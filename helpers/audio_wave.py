import math
import os
import queue
import threading
import time
import numpy as np
import pyaudio
from pydub import AudioSegment
import json
from PySide6.QtCore import Qt, QPointF, QRect, QPoint, QMetaObject
from PySide6.QtGui import QColor, QPainterPath, QFont
from scipy.interpolate import interp1d
from scipy.io import wavfile
from PySide6.QtWidgets import QVBoxLayout, QWidget, QFileDialog, QLabel, QScrollArea, QWidgetAction, QDialogButtonBox, QMessageBox
#import audio_wave_librosa_tools as awlt
from helpers.audio_wave_librosa_tools import Audio_Wave_Librosa_Tools

import pyqtgraph as pg

from helpers.joystick import BUF_MAX_SIZE, CHUNK_SIZE


def unique(list1):
    x = np.array(list1)
    return np.unique(x).tolist()

class PlotDataContainer():
    def __init__(self, parent, plotName, sample_rate = None , sample_data = [], pen = None, brush = None):
        if pen == None:
            pen = pg.mkPen(color=(255, 0, 0, 255), width=2)
            self.pen = pen

            self.original_indice_outer = pen
            self.selected_indice_outer = pg.mkPen(color=(255, 255, 255, 255), width=2)
        else:
            self.pen = pen
            self.original_indice_outer = pen
            self.selected_indice_outer = pg.mkPen(color=(255, 255, 255, 255), width=2)

        if brush == None:
            self.brush = pg.mkBrush(color=(255, 0, 0, 255))
            self.original_indice_middle = pg.mkBrush(color=(255, 0, 0, 255))
            self.selected_indice_middle = pg.mkBrush(color=(255, 0, 0, 255))
        else:
            self.brush = brush
            self.original_indice_middle = brush
            self.selected_indice_middle = brush

        self.plotName = plotName
        self.parent = parent
        if len(sample_data) == 0:
            self.plot_sample_data = parent.getOriginalSampleData().copy()
        else:
            self.plot_sample_data = sample_data
        if sample_rate == None:
            self.original_sample_rate = parent.getOriginalSampleRate()
        else:
            self.original_sample_rate = sample_rate
        self.currentFPS = parent.getCurrentFPS() # 25
        self.chunk_duration_ms = 1000 / self.currentFPS
        self.modified_sample_data = None
        self.modified_sample_time = None
        self.modified_sample_data_amp_strength = []
        self.original_modified_sample_data_amp_strength = []
        self.modified_sample_data_amp_strength_for_audio_playback = []

        self.modified_sample_data_amp_strength_modifiers = []

        self.original_sample_data_amp_strength_modifiers = []
        self.modified_sample_data_amp_strength_modifiers_multiplier = []
        self.modified_sample_data_amp_strength_modifiers_removed_vertices =[]
        self.chunk_amplitudes = []
        self.chunk_modified_sample_data_amp_strength_modifiers = []
        self.currently_selected_indices = []
        self.scatter_current_brushes_copy = []
        self.scatter_current_pens_copy = []
        self.modified_sample_time_amp_strength = None
        self.orginal_modified_sample_time_amp_strength = []
        self.chunk_scatter_brushes = []
        self.chunk_scatter_pens = []
        self.plotYRange = 1
        self.waveIndexPerFrame = 0
        self.waveAlpha = 255
        self.waveWidth = 2
        self.currentPlotMinValue = 0
        self.currentPlotMaxValue = 1
        self.plot_sample_data = self.convertToMono(self.plot_sample_data)
        self.setAmplitudeRangeMinuPlus()
        self.currentAmplitude = -1
        self.currentShift = 1
        self.currentAmpShift = 0
        self.currentXShift = 0
        self.currentMaxMultiplier = 0
        self.currentTempMin = 0
        self.setAmplitudeAndShift(amplitude=self.currentAmplitude, shift=self.currentShift, xshift=self.currentXShift, shouldChangeROIminmax=True)
        self.scatter = pg.ScatterPlotItem()
        self.hasHoverIndice = False
        self.isVisible = False
        self.isEditable = False
        self.should_synq_with_mediator = False
        #self.scatter.sigClicked.connect(self.clicked)
        #self.scatter.sigHovered.connect(self.hovered)

        self.lines = pg.PlotDataItem()

#        if len(self.scatter_current_brushes) != len(self.scatter_x_axis):
        #self.scatter_current_brushes = [self.original_indice_middle for _ in range(len(self.scatter_x_axis))]
        #self.scatter_current_pens = [self.original_indice_outer for _ in range(len(self.scatter_x_axis))]
        self.scatter_original_brushes = []
        self.scatter_original_pens = []
        self.scatter_current_brushes = []
        self.scatter_current_pens = []
        self.currentPlotColor = QColor(255, 255, 0, 255)
        self.currentScatterLinePenColor = self.pen

    def clicked(self, plot, points):
        print("Clicked a node")
    def hovered(self, plot, points):
        if len(points) != 0:
            print("Hovered a node:" + str(points))
    def getYAxisRange(self):
        return self.plotYRange
    def setYAxisRange(self, plotYRange):
        self.plotYRange = plotYRange
        self.setAmplitudeAndShift(shouldChangeROIminmax=True)

    def mouseDragEvent(self, ev, axis=None):
        print("dragging draging dragging!!")
        ev.accept()
    def getOriginalScatterPen(self):
        xAxisLen = len(self.getXaxis())
        if len(self.scatter_original_pens) != xAxisLen:
            self.scatter_original_pens = [self.original_indice_outer for _ in range(xAxisLen)]
        return self.scatter_original_pens

    def getOriginalScatterBrush(self):
        xAxisLen = len(self.getXaxis())
        if len(self.scatter_original_brushes) != xAxisLen:
            self.scatter_original_brushes = [self.original_indice_middle for _ in range(xAxisLen)]
        return self.scatter_original_brushes
    def isIndexSelected(self, indiceIndex):
        if indiceIndex in self.currently_selected_indices:
            return True
        else:
            return False
    def hasSelectedIndices(self):
        if len(self.currently_selected_indices) == 0:
            return False
        else:
            return True
    def emptySelectedIndices(self):
        self.setSelectedIndices([])
    def setSelectedIndices(self, indiceIndex, affectCopyAlso = False, selectedIndicesOriginal = None, selectAll = 0):
        if selectedIndicesOriginal == None:
            selectedIndicesOriginal = indiceIndex
        xAxisLen = len(self.getXaxis()) #len(self.chunk_scatter_brushes) #len(self.getXaxis())
        self.scatter_current_brushes = [self.original_indice_middle for _ in range(xAxisLen)]
        self.scatter_current_pens = [self.original_indice_outer for _ in range(xAxisLen)]
        self.chunk_scatter_brushes = [self.original_indice_middle for _ in range(len(self.chunk_scatter_brushes))]
        self.chunk_scatter_pens = [self.original_indice_outer for _ in range(len(self.chunk_scatter_pens))]

        if affectCopyAlso:
            self.scatter_current_brushes_copy = [self.original_indice_middle for _ in range(xAxisLen)]
            self.scatter_current_pens_copy = [self.original_indice_outer for _ in range(xAxisLen)]

        if selectAll == 1:
            self.currently_selected_indices = np.arange(len(self.modified_sample_data_amp_strength)).tolist()
            self.currently_selected_indices_original = np.arange(len(self.original_modified_sample_data_amp_strength)).tolist()

        elif self.parent.parent.setShiftKeyDown:
            #self.currently_selected_indices = self.currently_selected_indices + indiceIndex
            self.currently_selected_indices = self.currently_selected_indices + [i for i in indiceIndex if i not in self.currently_selected_indices]

            self.currently_selected_indices_original = self.currently_selected_indices_original + [i for i in selectedIndicesOriginal if i not in self.currently_selected_indices_original]
        elif self.parent.parent.setControlKeyDown and not self.parent.parent.setControlV:
            self.currently_selected_indices = [i for i in self.currently_selected_indices if i not in indiceIndex]
            self.currently_selected_indices_original = [i for i in self.currently_selected_indices_original if i not in selectedIndicesOriginal]
        else:
            self.currently_selected_indices = indiceIndex
            self.currently_selected_indices_original = selectedIndicesOriginal

        for index in self.currently_selected_indices:
            if index >= len(self.scatter_current_brushes):
                print("scatter_current_brushes is " + str(len(self.scatter_current_brushes)) + " large, but not large enough for index " + str(index) + " that is part of currently_selected_indices:" + str(self.currently_selected_indices))
            self.scatter_current_brushes[index] = self.selected_indice_middle
            self.scatter_current_pens[index] = self.selected_indice_outer
            if affectCopyAlso:
                self.scatter_current_brushes_copy[index] = self.selected_indice_middle
                self.scatter_current_pens_copy[index] = self.selected_indice_outer

        for index in self.currently_selected_indices_original:
            self.chunk_scatter_brushes[index] = self.selected_indice_middle
            self.chunk_scatter_pens[index] = self.selected_indice_outer
            #if affectCopyAlso:
            #    self.scatter_current_brushes_copy[index] = self.selected_indice_middle
            #    self.scatter_current_pens_copy[index] = self.selected_indice_outer


    def setHoverIndice(self, indiceIndex):
        if self.hasHoverIndice and len(indiceIndex) == 0:
            self.hasHoverIndice = False
            self.scatter_current_brushes = self.scatter_current_brushes_copy
            self.scatter_current_pens = self.scatter_current_pens_copy
        elif not self.hasHoverIndice:
            if len(indiceIndex) > 0:
                self.hasHoverIndice = True
                self.scatter_current_brushes_copy = self.scatter_current_brushes.copy()
                self.scatter_current_pens_copy = self.scatter_current_pens.copy()
                for index in indiceIndex:
                    #xShift = self.getCurrentXShift()
                    #if xShift < 0:
                    #    index = index - xShift
                    self.scatter_current_brushes[index] = self.selected_indice_middle
                    self.scatter_current_pens[index] = self.selected_indice_outer

    def unSelectAllIndices(self):
        xAxisLen = len(self.getXaxis())
        self.scatter_current_brushes = [self.original_indice_middle for _ in range(xAxisLen)]
        self.scatter_current_pens = [self.original_indice_outer for _ in range(xAxisLen)]
        self.currently_selected_indices = []

    def addValueToIndices(self, value):
        if len(self.modified_sample_data_amp_strength_modifiers) == 0:
            print("modified_sample_data_amp_strength_modifiers was not allocated yet!")
            self.modified_sample_data_amp_strength_modifiers = np.empty(len(self.modified_sample_data_amp_strength))
            self.modified_sample_data_amp_strength_modifiers.fill(0)

        if len(self.currently_selected_indices) != 0:
            for index in self.currently_selected_indices:
                if (self.currentAmplitude - self.currentAmpShift) != 0:
                    self.modified_sample_data_amp_strength_modifiers[index] = self.modified_sample_data_amp_strength_modifiers[index] + (value / (self.currentAmplitude - self.currentAmpShift))  #amplitude_change
                else:
                    self.modified_sample_data_amp_strength_modifiers[index] = self.modified_sample_data_amp_strength_modifiers[index] + value

        if len(self.currently_selected_indices_original) != 0:
            for index in self.currently_selected_indices_original:
                if (self.currentAmplitude - self.currentAmpShift) != 0:
                    self.chunk_modified_sample_data_amp_strength_modifiers[index] = self.chunk_modified_sample_data_amp_strength_modifiers[index] + (value / (self.currentAmplitude - self.currentAmpShift))  #amplitude_change
                else:
                    self.chunk_modified_sample_data_amp_strength_modifiers[index] = self.chunk_modified_sample_data_amp_strength_modifiers[index] + value

        #else:
        #    #How do I solve so that the indices (modified or not from original), are not collectively transformed to the absolute value of the Amplitude change input box?
        #    self.modified_sample_data_amp_strength_modifiers = self.modified_sample_data_amp_strength_modifiers  + (value / (self.currentAmplitude - self.currentAmpShift)) #(amplitude - self.modified_sample_data_amp_strength_modifiers) # + amplitude_change
    def setIndiceDragValue(self, index, indexValue, dragDistance):
        if index != None:
            #xShift = self.getCurrentXShift()
            #if xShift < 0:
            #    index = index - xShift
            self.modified_sample_data_amp_strength[index] = indexValue #/self.currentAmplitude
        if len(self.currently_selected_indices) != 0:
            for indexSelectedIndices in self.currently_selected_indices:
                if indexSelectedIndices != index:
                    #xShift = self.getCurrentXShift()
                    #if xShift < 0:
                    #    indexSelectedIndices = indexSelectedIndices + xShift
                    self.modified_sample_data_amp_strength[indexSelectedIndices] = self.modified_sample_data_amp_strength[indexSelectedIndices] + dragDistance #(value * self.currentAmplitude)  #amplitude_change

    def setIndiceValue(self, index, indexValue):
        if index != None:
            dragDistance = indexValue - self.modified_sample_data_amp_strength[index]
            self.modified_sample_data_amp_strength[index] = indexValue
            self.modified_sample_data_amp_strength_modifiers[index] = self.modified_sample_data_amp_strength_modifiers[index] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
        if len(self.currently_selected_indices) != 0:
            for indexSelectedIndice in self.currently_selected_indices:
                dragDistance = indexValue - self.modified_sample_data_amp_strength[indexSelectedIndice]
                #self.modified_sample_data_amp_strength[indexSelectedIndice] = indexValue
                self.modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = self.modified_sample_data_amp_strength_modifiers[indexSelectedIndice] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
            for indexSelectedIndice in self.currently_selected_indices_original:
                dragDistance = indexValue - self.original_modified_sample_data_amp_strength[indexSelectedIndice] # self.chunk_amplitudes[indexSelectedIndice]
                self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndice] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))

    def setIndiceValueSpecific(self, sample_data_array, data_index, indexValue):
        for indexIndices in data_index:
            dragDistance = indexValue - sample_data_array[indexIndices]
            self.chunk_modified_sample_data_amp_strength_modifiers[indexIndices] = self.chunk_modified_sample_data_amp_strength_modifiers[indexIndices] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))

    def setIndiceValueFromTo(self, index, fromValue, toValue, value):
        if fromValue < toValue:
            tempFrom = fromValue
            fromValue = toValue
            toValue = tempFrom
        if len(self.currently_selected_indices) != 0:
            for indexSelectedIndice in self.currently_selected_indices:
                if (self.modified_sample_data_amp_strength[indexSelectedIndice] <= fromValue) and (self.modified_sample_data_amp_strength[indexSelectedIndice] >= toValue):
                    dragDistance = value - self.modified_sample_data_amp_strength[indexSelectedIndice]
                    #self.modified_sample_data_amp_strength[indexSelectedIndice] = value
                    self.modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = self.modified_sample_data_amp_strength_modifiers[indexSelectedIndice] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
            index = 0
            for indexSelectedIndice in self.currently_selected_indices_original:
                indirect_sample_value = self.original_modified_sample_data_amp_strength[indexSelectedIndice]
                if (indirect_sample_value <= fromValue) and (indirect_sample_value >= toValue):
                    dragDistance = value - indirect_sample_value #self.modified_sample_data_amp_strength[index]
                    #self.modified_sample_data_amp_strength[indexSelectedIndice] = value
                    self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndice] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
                index += 1
        else:
            i = 0
            for indexSelectedIndice in self.modified_sample_data_amp_strength:
                if (indexSelectedIndice <= fromValue) and (indexSelectedIndice >= toValue):
                    dragDistance = value - indexSelectedIndice
                    #self.modified_sample_data_amp_strength[i] = value
                    if (self.currentAmplitude - self.currentAmpShift) != 0:
                        self.modified_sample_data_amp_strength_modifiers[i] = self.modified_sample_data_amp_strength_modifiers[i] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
                i += 1
            i = 0
            for indexSelectedIndice in self.original_modified_sample_data_amp_strength:
                if (indexSelectedIndice <= fromValue) and (indexSelectedIndice >= toValue):
                    dragDistance = value - indexSelectedIndice
                    #self.modified_sample_data_amp_strength[i] = value
                    if (self.currentAmplitude - self.currentAmpShift) != 0:
                        self.chunk_modified_sample_data_amp_strength_modifiers[i] = self.chunk_modified_sample_data_amp_strength_modifiers[i] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
                i += 1

    def getIndiceValueHighAmp(self):
        if (self.currentAmplitude + self.currentShift) >= (self.currentAmpShift + self.currentShift):
            indexValue = (self.currentAmplitude + self.currentShift)
        else:
            indexValue = (self.currentAmpShift + self.currentShift)
        return indexValue
    def setIndiceValueHighAmp(self,index):
        if (self.currentAmplitude + self.currentShift) >= (self.currentAmpShift + self.currentShift):
            indexValue = (self.currentAmplitude + self.currentShift)
        else:
            indexValue = (self.currentAmpShift + self.currentShift)
        if index != None:
            dragDistance = indexValue - self.modified_sample_data_amp_strength[index]
            #self.modified_sample_data_amp_strength[index] = indexValue
            self.modified_sample_data_amp_strength_modifiers[index] = self.modified_sample_data_amp_strength_modifiers[index] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
        if len(self.currently_selected_indices) != 0:
            for indexSelectedIndice in self.currently_selected_indices:
                dragDistance = indexValue - self.modified_sample_data_amp_strength[indexSelectedIndice]
                self.modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = self.modified_sample_data_amp_strength_modifiers[indexSelectedIndice] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
            for indexSelectedIndice in self.currently_selected_indices_original:
                dragDistance = indexValue - self.original_modified_sample_data_amp_strength[indexSelectedIndice] # self.chunk_amplitudes[indexSelectedIndice]
                self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndice] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))

    def getIndiceValueLowAmp(self):
        if (self.currentAmplitude + self.currentShift) <= (self.currentAmpShift + self.currentShift):
            indexValue = (self.currentAmplitude + self.currentShift)
        else:
            indexValue = (self.currentAmpShift + self.currentShift)
        return indexValue

    def setIndiceValueLowAmp(self,index):
        if (self.currentAmplitude + self.currentShift) <= (self.currentAmpShift + self.currentShift):
            indexValue = (self.currentAmplitude + self.currentShift)
        else:
            indexValue = (self.currentAmpShift + self.currentShift)
        if index != None:
            dragDistance = indexValue - self.modified_sample_data_amp_strength[index]
            #self.modified_sample_data_amp_strength[index] = indexValue
            self.modified_sample_data_amp_strength_modifiers[index] = self.modified_sample_data_amp_strength_modifiers[index] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
        if len(self.currently_selected_indices) != 0:
            for indexSelectedIndice in self.currently_selected_indices:
                dragDistance = indexValue - self.modified_sample_data_amp_strength[indexSelectedIndice]
                self.modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = self.modified_sample_data_amp_strength_modifiers[indexSelectedIndice] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
            for indexSelectedIndice in self.currently_selected_indices_original:
                dragDistance = indexValue - self.original_modified_sample_data_amp_strength[indexSelectedIndice] # self.chunk_amplitudes[indexSelectedIndice]
                self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndice] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))

    def setIndiceValueMiddleAmp(self,index):
        indexValue = (self.currentAmplitude + self.currentAmpShift)/2 + self.currentShift
        if index != None:
            dragDistance = indexValue - self.modified_sample_data_amp_strength[index]
            #self.modified_sample_data_amp_strength[index] = indexValue
            self.modified_sample_data_amp_strength_modifiers[index] = self.modified_sample_data_amp_strength_modifiers[index] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
        if len(self.currently_selected_indices) != 0:
            for indexSelectedIndice in self.currently_selected_indices:
                dragDistance = indexValue - self.modified_sample_data_amp_strength[indexSelectedIndice]
                self.modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = self.modified_sample_data_amp_strength_modifiers[indexSelectedIndice] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
            for indexSelectedIndice in self.currently_selected_indices_original:
                dragDistance = indexValue - self.original_modified_sample_data_amp_strength[indexSelectedIndice] # self.chunk_amplitudes[indexSelectedIndice]
                self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndice] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
    def setIndiceValueOrgAmp(self,index):
        if index != None:
            #dragDistance = indexValue - self.modified_sample_data_amp_strength[index]
            #self.modified_sample_data_amp_strength[index] = indexValue
            self.modified_sample_data_amp_strength_modifiers[index] = 0 #self.modified_sample_data_amp_strength_modifiers[index] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
        if len(self.currently_selected_indices) != 0:
            for indexSelectedIndice in self.currently_selected_indices:
                self.modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = 0#self.modified_sample_data_amp_strength_modifiers[indexSelectedIndice] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))

            for indexSelectedIndice in self.currently_selected_indices_original:
                self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = 0#self.modified_sample_data_amp_strength_modifiers[indexSelectedIndice] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))

    def setIndiceValueOnCadenceSteps(self, cadence_change_audio_value, cadence_change_audio_gap_value, cadence_change_audio_other_value):
        if cadence_change_audio_gap_value <= 0:
            return
        else:
            cadence_change_audio_gap_value = int(cadence_change_audio_gap_value)

        sorted_currently_selected_indices_original = sorted(self.currently_selected_indices_original)
        sorted_currently_selected_indices = sorted(self.currently_selected_indices)
        corrected_beat_value = self.calculateChunkAmplitudeFromCurrentValue(cadence_change_audio_value)
        corrected_other_value = self.calculateChunkAmplitudeFromCurrentValue(cadence_change_audio_other_value)

        #Figure out which is the indice in the selection that is on the first cadence line inside the selection
        if len(self.currently_selected_indices) != 0:
            selected_indexes = sorted(self.currently_selected_indices)
            xShift = self.getCurrentXShift()
            current_cadence = self.parent.parent.parent.DeforumationMotions.cadence
            minIndex = sorted_currently_selected_indices_original[0]
            maxIndex = sorted_currently_selected_indices_original[len(selected_indexes)-1]
            gap_index = 0
            for indexSelectedIndice in range(minIndex,maxIndex+1):
                if (indexSelectedIndice+xShift) % current_cadence == 0:
                    if gap_index == 0:
                        self.chunk_amplitudes[indexSelectedIndice] = corrected_beat_value #paste_values[paste_index]
                        self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = 0 #copyBuffer_modifiers[paste_index]
                    else:
                        self.chunk_amplitudes[indexSelectedIndice] = corrected_other_value #paste_values[paste_index]
                        self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = 0 #copyBuffer_modifiers[paste_index]

                    gap_index += 1
                    if gap_index == cadence_change_audio_gap_value:
                        gap_index = 0
                else:
                    self.chunk_amplitudes[indexSelectedIndice] = corrected_other_value  # paste_values[paste_index]
                    self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndice] = 0  # copyBuffer_modifiers[paste_index]
                self.removeFromRemovedVertices([indexSelectedIndice])

    def resetIndicesMofifier(self, index):
        self.modified_sample_data_amp_strength_modifiers[index] = 0

#self.currentDragPlot.setNewIndicesMultiplierValue(self.currentDragIndiceIndex, currPosY)
    def setNewIndicesMultiplierValue(self, index, dragDistance, currentDragIndiceIndexOriginalPosition):
        #xShift = self.getCurrentXShift()
        #if xShift < 0:
        #    currentDragIndiceIndexOriginalPosition = currentDragIndiceIndexOriginalPosition - xShift


        if index != None:
            #xShift = self.getCurrentXShift()
            #if xShift < 0:
            #    index = index - xShift
            self.modified_sample_data_amp_strength_modifiers[index] = self.modified_sample_data_amp_strength_modifiers[index] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
            self.chunk_modified_sample_data_amp_strength_modifiers[currentDragIndiceIndexOriginalPosition] = self.chunk_modified_sample_data_amp_strength_modifiers[currentDragIndiceIndexOriginalPosition] + (dragDistance / (self.currentAmplitude - self.currentAmpShift))
        if len(self.currently_selected_indices) != 0:
            for indexSelectedIndices in self.currently_selected_indices:
                if indexSelectedIndices != index:
                    self.modified_sample_data_amp_strength_modifiers[indexSelectedIndices] = self.modified_sample_data_amp_strength_modifiers[indexSelectedIndices] + (dragDistance / (self.currentAmplitude - self.currentAmpShift)) #(value * self.currentAmplitude)  #amplitude_change
            for indexSelectedIndices in self.currently_selected_indices_original:
                if indexSelectedIndices != currentDragIndiceIndexOriginalPosition:
                    self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndices] = self.chunk_modified_sample_data_amp_strength_modifiers[indexSelectedIndices] + (dragDistance / (self.currentAmplitude - self.currentAmpShift)) #(value * self.currentAmplitude)  #amplitude_change

    def getCurrentScatterPen(self):
        xAxisLen = len(self.getXaxis())
        if xAxisLen > len(self.scatter_current_pens):
            self.scatter_current_pens = [self.original_indice_outer for _ in range(xAxisLen)]

        return self.scatter_current_pens
    def getCurrentScatterLinePenColor(self):
        return self.currentScatterLinePenColor
    def getCurrentScatterBrush(self):
        xAxisLen = len(self.getXaxis())
        if len(self.scatter_current_brushes) != xAxisLen:
            self.scatter_current_brushes = [self.original_indice_middle for _ in range(xAxisLen)]
        return self.scatter_current_brushes

    def setPlotColor(self, rgb):
            self.currentPlotColor = rgb
            self.pen = pg.mkPen(color=rgb)
            self.currentScatterLinePenColor = self.pen
            self.original_indice_outer = pg.mkPen(color=rgb, width=2)
            self.selected_indice_outer = pg.mkPen(color=(255, 255, 255, 255), width=2)

            self.brush = pg.mkBrush(color=(255, 0, 0, 255))
            self.original_indice_middle = pg.mkBrush(color=rgb)
            self.selected_indice_middle = pg.mkBrush(color=rgb)
    def getPlotColor(self):
            return self.currentPlotColor
    def getScatter(self):
        return self.scatter

    def getLines(self):
        return self.lines

    def convertToMono(self, sample_data):
        if sample_data.ndim == 2:  # Check if stereo
            sample_data = sample_data.mean(axis=1)  # Convert to mono
        return sample_data
    def setAmplitudeRangeMinuPlus(self):
        #Make it go from -1 to 1
        #self.modified_sample_data = self.original_sample_data.copy()

        if self.modified_sample_data == None:
            self.modified_sample_data = self.plot_sample_data.copy()
        if self.plot_sample_data.dtype == np.int16:
            self.modified_sample_data = self.modified_sample_data / 32768.0  # Convert 16-bit integers to -1 to 1 range
        elif self.plot_sample_data.dtype == np.int32:
            self.modified_sample_data = self.modified_sample_data / 2147483648.0

    def setAmplitudeAndShift(self, amplitude = None, shift = None, ampshift = None, xshift=None, shouldChangeROIminmax = False):
        if amplitude == None:
            amplitude = self.currentAmplitude #self.parent.getCurrentAmplitude() #self.parent.currentAmplitude
        if shift == None:
            shift = self.currentShift #self.parent.currentShift
        if ampshift == None:
            ampshift = self.currentAmpShift #self.parent.currentShift
        if xshift == None:
            xshift = self.currentXShift #self.parent.currentShift
        #shouldShiftCurve = False
        #if (self.currentAmplitude > 0 and amplitude < 0) or (self.currentAmplitude < 0 and amplitude > 0):
        #    shouldShiftCurve = True


        #amplitude_change = amplitude - self.currentAmplitude # 1 - -1 = -2 ... 1 - -1 = 2
        #shift_change = self.currentShift - shift
        self.currentAmplitude = amplitude
        self.currentShift = shift
        self.currentAmpShift = ampshift
        self.currentXShift = xshift
        # Define chunk size in milliseconds and calculate chunk size in samples
        fps = self.parent.getCurrentFPS() #self.currentFPS
        self.chunk_duration_ms = 1000/fps  #40
        chunk_size_samples = int((self.original_sample_rate * self.chunk_duration_ms) / 1000)
        # Initialize an array to hold the average amplitude for each chunk

        if len(self.chunk_modified_sample_data_amp_strength_modifiers) == 0:
            chunk_amplitudes = []
            self.modified_sample_data_amp_strength = []
            self.modified_sample_data_amp_strength = self.modified_sample_data.copy()
            self.modified_sample_data_amp_strength = np.abs(self.modified_sample_data_amp_strength)

            #if firstRun:
            for i in range(0, len(self.modified_sample_data_amp_strength), chunk_size_samples):
                chunk = self.modified_sample_data_amp_strength[i:i + chunk_size_samples]
                chunk_amplitude = np.mean(np.abs(chunk))
                chunk_amplitudes.append(chunk_amplitude)
            self.chunk_amplitudes = chunk_amplitudes
            self.chunk_modified_sample_data_amp_strength_modifiers = np.empty(len(self.chunk_amplitudes))
            self.chunk_modified_sample_data_amp_strength_modifiers.fill(0)
        if len(self.chunk_scatter_brushes) == 0:
            self.chunk_scatter_brushes = [self.original_indice_middle for _ in range(len(self.chunk_amplitudes))]
            self.chunk_scatter_pens = [self.original_indice_outer for _ in range(len(self.chunk_amplitudes))]

        self.modified_sample_data_amp_strength_modifiers = self.chunk_modified_sample_data_amp_strength_modifiers.copy()
        self.modified_sample_data_amp_strength = self.chunk_amplitudes.copy()
        self.scatter_current_brushes = self.chunk_scatter_brushes.copy()
        self.scatter_current_pens = self.chunk_scatter_pens.copy()

        axisYRange = self.getYAxisRange()
        amplitude = amplitude - self.currentAmpShift
        tempMin = np.min(self.modified_sample_data_amp_strength)
        self.currentTempMin = tempMin
        self.modified_sample_data_amp_strength = self.modified_sample_data_amp_strength - tempMin #For Bend
        tempMax = np.max(self.modified_sample_data_amp_strength)
        maxMultiplier = axisYRange / tempMax * amplitude
        self.currentMaxMultiplier = maxMultiplier

        self.modified_sample_data_amp_strength = self.modified_sample_data_amp_strength * maxMultiplier  # For Amplitude
        self.modified_sample_data_amp_strength = self.modified_sample_data_amp_strength + (self.modified_sample_data_amp_strength_modifiers * amplitude)#self.currentAmplitude)


        #Shift
        self.modified_sample_data_amp_strength = self.modified_sample_data_amp_strength + shift + self.currentAmpShift
        self.original_modified_sample_data_amp_strength = self.modified_sample_data_amp_strength.copy()

        #blaha = self.original_modified_sample_data_amp_strength[index] - shift - self.currentAmpShift  - (self.modified_sample_data_amp_strength_modifiers[index] * amplitude)

        self.modified_sample_data_amp_strength = self.removeVertices(self.modified_sample_data_amp_strength, self.modified_sample_data_amp_strength_modifiers_removed_vertices) #TESTING TESTING

        if shouldChangeROIminmax:
            self.currentPlotMinValue = np.min(self.modified_sample_data_amp_strength)
            self.currentPlotMaxValue = np.max(self.modified_sample_data_amp_strength)

        # Create a time axis for the chunks
        self.modified_sample_time_amp_strength = np.arange(len(self.chunk_amplitudes)) * (self.chunk_duration_ms / 1000.0) + ((self.chunk_duration_ms / 1000.0)*self.currentXShift) #TESTING TESTING
        self.orginal_modified_sample_time_amp_strength = self.modified_sample_time_amp_strength
        self.modified_sample_time_amp_strength = self.removeVertices(self.modified_sample_time_amp_strength, self.modified_sample_data_amp_strength_modifiers_removed_vertices) #TESTING TESTING

        self.scatter_current_brushes = self.removeVertices(self.scatter_current_brushes, self.modified_sample_data_amp_strength_modifiers_removed_vertices)
        self.scatter_current_pens = self.removeVertices(self.scatter_current_pens, self.modified_sample_data_amp_strength_modifiers_removed_vertices)

        pass

    def calculateChunkAmplitudeFromCurrentValue(self, value):
        # Calculate backwards
        value = value - self.currentShift - self.currentAmpShift
        value = value / self.currentMaxMultiplier
        value = value + self.currentTempMin
        return value

    def insertBeatFrom(self, beat_value, other_value, number_of_beats_value, bpm_value):
        if len(self.currently_selected_indices_original) > 0:
            sorted_currently_selected_indices_original = sorted(self.currently_selected_indices_original)
            sorted_currently_selected_indices = sorted(self.currently_selected_indices)
            indiceIndex_original = sorted_currently_selected_indices_original[0]
            indiceIndex = sorted_currently_selected_indices[0]

            fps = self.parent.getCurrentFPS()
            frames_per_beat = round((60 / bpm_value) / (1 / fps))
            corrected_beat_value = self.calculateChunkAmplitudeFromCurrentValue(beat_value)
            corrected_other_value = self.calculateChunkAmplitudeFromCurrentValue(other_value)
            lastIndiceIndex = 0
            lastIndiceIndex_original = 0

            copyBuffer = np.empty(4*number_of_beats_value - number_of_beats_value + 1)
            copyBuffer_modifiers = np.empty(4*number_of_beats_value- number_of_beats_value + 1)  # plotContainer[self.parent.selectedPlot].chunk_modified_sample_data_amp_strength_modifiers[selected_points_original]
            copyBuffer_modifiers.fill(0)  # 0,0,0,0

            #copyBuffer_x = np.empty(4*number_of_beats_value)
            copyBuffer_x = []
            copyBuffer_x_original = []
            for n in range(0,number_of_beats_value):
                if n == 0:
                    copyBuffer[0 + (4 * n)] = corrected_beat_value
                    copyBuffer[3 + (4 * n)] = corrected_beat_value
                    copyBuffer[1 + (4 * n)] = corrected_other_value
                    copyBuffer[2 + (4 * n)] = corrected_other_value
                    copyBuffer_x = copyBuffer_x + [indiceIndex+(4*n),indiceIndex+1+(4*n),indiceIndex+2+(4*n),indiceIndex+3+(4*n)] # = [indiceIndex, indiceIndex+1, indiceIndex+2, indiceIndex+3] #3,4,5,6
                    copyBuffer_x_original = copyBuffer_x_original + [indiceIndex_original, indiceIndex_original+1, indiceIndex_original+frames_per_beat-1, indiceIndex_original+frames_per_beat] #3,4,22,23
                elif n == 1:
                    copyBuffer[0 + (4 * n)] = corrected_other_value
                    copyBuffer[1 + (4 * n)] = corrected_other_value
                    copyBuffer[2 + (4 * n)] = corrected_beat_value
                    copyBuffer_x = copyBuffer_x + [indiceIndex+(4*n),indiceIndex+1+(4*n),indiceIndex+2+(4*n)] # = [indiceIndex, indiceIndex+1, indiceIndex+2, indiceIndex+3] #3,4,5,6
                    copyBuffer_x_original = copyBuffer_x_original + [indiceIndex_original+1, indiceIndex_original+frames_per_beat-1, indiceIndex_original+frames_per_beat] #3,4,22,23
                else:
                    copyBuffer[7 + (3 * (n-2))] = corrected_other_value
                    copyBuffer[8 + (3 * (n-2))] = corrected_other_value
                    copyBuffer[9 + (3 * (n-2))] = corrected_beat_value

                    copyBuffer_x = copyBuffer_x + [indiceIndex+7+(3 * (n-2)),indiceIndex+8+(3 * (n-2)),indiceIndex+9+(3 * (n-2))] # = [indiceIndex, indiceIndex+1, indiceIndex+2, indiceIndex+3] #3,4,5,6
                    copyBuffer_x_original = copyBuffer_x_original + [indiceIndex_original+1, indiceIndex_original+frames_per_beat-1, indiceIndex_original+frames_per_beat] #3,4,22,23

                indiceIndex_original += frames_per_beat
            lastIndiceIndex, lastIndiceIndex_original = self.insertValuesFrom(copyBuffer, copyBuffer_x, copyBuffer_x_original, copyBuffer_modifiers)
            #indiceIndex_original += frames_per_beat
            #indiceIndex += 4
            #self.currently_selected_indices_original = [indiceIndex_original]
            #self.currently_selected_indices = [indiceIndex]

            return lastIndiceIndex, lastIndiceIndex_original
        return -1, -1

    def insertValuesFrom(self, paste_values, paste_values_x, paste_values_x_original, copyBuffer_modifiers):

        if len(self.currently_selected_indices_original) > 0:
            sorted_currently_selected_indices_original = sorted(self.currently_selected_indices_original)
            sorted_currently_selected_indices = sorted(self.currently_selected_indices)
            indiceIndex_original = sorted_currently_selected_indices_original[0]
            indiceIndex = sorted_currently_selected_indices[0]
            lastIndiceIndex_original = indiceIndex_original + (paste_values_x_original[len(paste_values_x_original)-1] - paste_values_x_original[0]) #indiceIndex_original + len(paste_values)-1
            lastIndiceIndex = indiceIndex + (paste_values_x[len(paste_values_x)-1] - paste_values_x[0])
            #Check if paste is going over current length of self.chunk_amplitudes
            if lastIndiceIndex_original >= len(self.chunk_amplitudes):
                #expand self.chunk_amplitudes
                expand_this_much = lastIndiceIndex_original - len(self.chunk_amplitudes) + 1
                print("Expanding arrays with this many: " +str(expand_this_much))
                zero_array = np.empty(expand_this_much)
                zero_array.fill(0)

                #self.chunk_amplitudes = np.append(self.chunk_amplitudes, zero_array)
                self.chunk_amplitudes = self.chunk_amplitudes + zero_array.tolist()
                self.original_modified_sample_data_amp_strength = np.append(self.original_modified_sample_data_amp_strength, zero_array)
                self.chunk_modified_sample_data_amp_strength_modifiers = np.append(self.chunk_modified_sample_data_amp_strength_modifiers, zero_array)
                self.chunk_scatter_brushes = np.append(self.chunk_scatter_brushes, zero_array)
                self.chunk_scatter_pens = np.append(self.chunk_scatter_pens, zero_array)
                print("Now chunk_scatter_brushes is " + str(len(self.chunk_scatter_brushes)) + " large.")
            else:
                print("Did not need yo expand arrays!")

            from_val = paste_values_x_original[0]
            to_val = paste_values_x_original[len(paste_values_x_original)-1]
            index = indiceIndex_original
            paste_index = 0
            print("Copying from index " + str(from_val) + " to index" + str(to_val))
            for n in range(from_val, to_val+1):
                if n in paste_values_x_original:
                    self.chunk_amplitudes[index] = paste_values[paste_index]
                    self.chunk_modified_sample_data_amp_strength_modifiers[index] = copyBuffer_modifiers[paste_index]
                    paste_index += 1
                else:
                    val = self.chunk_amplitudes[n]
                    self.chunk_amplitudes[index] = val
                    val = self.chunk_modified_sample_data_amp_strength_modifiers[n]
                    self.chunk_modified_sample_data_amp_strength_modifiers[index] = val

                #print("original self.chunk_modified_sample_data_amp_strength_modifiers["+str(n)+"] => " + str(self.chunk_modified_sample_data_amp_strength_modifiers[n]))
                if not n in paste_values_x_original:
                    #print("Index " + str(index) + " should be added to not visible array")
                    self.addToRemovedVertices([index])
                else:
                    self.removeFromRemovedVertices([index])
                index += 1
            return lastIndiceIndex, lastIndiceIndex_original
        else:
            print("No indices selected, can't paste values")
    def removeVertices(self, data_array, vertices):
        data_array = np.delete(data_array, vertices)
        #for n in vertices:
        #    np.delete(data_array, n, axis=0)
        #index = 0
        #for n in range(len(vertices)):
        #    data_array = np.delete(data_array, vertices[index], axis=0)
        #    index += 1
        return data_array

    def removeVerticesFromVerticeDeleteList(self, data_array, verticeIndex):
        last_array = data_array[len(data_array)-1]
        modified_array = []
        for n in last_array:
            if n != verticeIndex:
                modified_array.append(n)
        #modified_array = np.delete(modified_array, verticeIndex)

        data_array = data_array[:len(data_array)-1]
        if len(modified_array) !=0:
            data_array.append(np.array(modified_array)) #append(modified_array)

        return data_array


    def insertIndiceInTime(self, time_value, new_vertex_index, sample_value=0):
        modified_sample_data_amp_strength_modifiers_removed_vertices = []
        for n in self.modified_sample_data_amp_strength_modifiers_removed_vertices:
            if n != new_vertex_index:
                modified_sample_data_amp_strength_modifiers_removed_vertices.append(n)
        self.modified_sample_data_amp_strength_modifiers_removed_vertices = modified_sample_data_amp_strength_modifiers_removed_vertices

        '''for x in range(len(self.modified_sample_time_amp_strength)):
            if self.modified_sample_time_amp_strength[x] == time_value:
                print("There is already an index here, so can't insert")
                return False
            if time_value < self.modified_sample_time_amp_strength[x]:
                print("Should be inserted after indice:" + str(x))
                kalle = self.modified_sample_data_amp_strength_modifiers_removed_vertices
                self.modified_sample_time_amp_strength = np.append(np.append(self.modified_sample_time_amp_strength[:x], time_value), self.modified_sample_time_amp_strength[x:])
                self.modified_sample_data_amp_strength = np.append(np.append(self.modified_sample_data_amp_strength[:x], sample_value), self.modified_sample_data_amp_strength[x:])
                self.modified_sample_data_amp_strength_modifiers = np.append(np.append(self.modified_sample_data_amp_strength_modifiers[:x], 0), self.modified_sample_data_amp_strength_modifiers[x:])
                self.modified_sample_data_amp_strength_modifiers_removed_vertices = self.removeVerticesFromVerticeDeleteList(self.modified_sample_data_amp_strength_modifiers_removed_vertices, new_vertex_index)
                #np.insert(self.modified_sample_time_amp_strength
                return True'''

        return True



    def removeFromRemovedVertices(self, vertice_list):
        if len(vertice_list) != 0:
            for n in vertice_list:
                if n in self.modified_sample_data_amp_strength_modifiers_removed_vertices:
                    self.modified_sample_data_amp_strength_modifiers_removed_vertices.remove(n)
    def addToRemovedVertices(self, vertice_list = []):
        if len(vertice_list) != 0:
            self.modified_sample_data_amp_strength_modifiers_removed_vertices += vertice_list
            self.modified_sample_data_amp_strength_modifiers_removed_vertices = unique(self.modified_sample_data_amp_strength_modifiers_removed_vertices)
        elif len(self.currently_selected_indices) != 0:
            vertice_list = self.currently_selected_indices_original.copy()
            self.modified_sample_data_amp_strength_modifiers_removed_vertices += vertice_list#.append(vertices)
            self.modified_sample_data_amp_strength_modifiers_removed_vertices = unique(self.modified_sample_data_amp_strength_modifiers_removed_vertices)
    def isIndiceVisible(self, index):
        if index in self.modified_sample_data_amp_strength_modifiers_removed_vertices:
            return False
        return True

    def getcurrentPlotMinValue(self):
        return self.currentPlotMinValue
    def getcurrentPlotMaxValue(self):
        return self.currentPlotMaxValue
    def getCurrentXShift(self):
        return self.currentXShift
    def getXaxis(self):
        return self.modified_sample_time_amp_strength
    def getYaxis(self):
        return self.modified_sample_data_amp_strength

    def getYaxisOriginal(self):
        return self.original_modified_sample_data_amp_strength
    def getXaxisOriginal(self):
        return self.orginal_modified_sample_time_amp_strength


    def getYaxisForAudioPlayback(self):
        return self.modified_sample_data_amp_strength_for_audio_playback

    def getPlotDataLen(self):
        return len(self.modified_sample_time_amp_strength)
    def setCurrentAmplitude(self, amplitude):
        self.currentAmplitude = amplitude

    def getCurrentAmplitude(self):
        return self.currentAmplitude

    def setCurrentShift(self, shift):
        self.currentShift = shift
    def getCurrentShift(self):
        return self.currentShift
    def setCurrentAmpShift(self, ampshift):
        self.currentAmpShift = ampshift
    def getCurrentAmpShift(self):
        return self.currentAmpShift
    def getSelectedIndices(self):
        return self.currently_selected_indices

    def getSelectedIndicesOriginal(self):
        return self.currently_selected_indices_original

class AudioWaveDataContainer():
    def __init__(self, parent):
        self.plotDataContainer = {}
        self.parent = parent
        self.currentAudioFilePath = None
        self.original_sample_data = None
        self.original_sample_rate = 0
        self.metronome_sample_data = None
        self.metronome_sample_rate = 0
        self.currentFPS = 25
        self.chunk_duration_ms = 1000 / 25
        self.modified_sample_data = None
        self.modified_sample_time = None
        self.waveIndexPerFrame = 0
        self.waveAlpha = 30
        self.currentMinValue = -1
        self.currentMaxValue = 1
        self.currentAmplitude = -1
        self.currentShift = 1
        self.currentAudioPlayerStartPosition = 0
        self.currentAudioPlayerStartPositionXaxis = 0
        self.startPositionAudioPlayerStartPositionXaxis = 0
        self.shouldPlayAudio = False
        self.shouldPlayAudioRememberPosition = False
        self.shouldCloseAudioPlayer = False
        self.currentAudioPlayerNewPosition = False
        self.currentTotalAudioVideoFrames = 0
        self.audioplayer_t = None

    def metronomePlayer(self):

        '''while True:
            startTime = time.time()
            play_callback(beep)
            endTime = time.time() - startTime
            time.sleep(60 / bpm - endTime)'''
        chunksize = int(self.metronome_sample_rate / self.currentFPS)
        array = self.metronome_sample_data
        fs = self.metronome_sample_rate
        index = 0
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=len(array.shape), rate=fs, output=True)
        while len(array) > index * chunksize:
            stream.write(array[index * chunksize:(index + 1) * chunksize].tobytes())
            index += 1

        stream.stop_stream()
        stream.close()
        p.terminate()

    def playMetronomeSound(self):
        self.metronome_player_stopped = threading.Event()
        self.metronome_player_q = queue.Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK_SIZE)))
        self.metronomeplayer_t = threading.Thread(target=self.metronomePlayer)
        self.metronomeplayer_t.start()

    def audioPlayer(self, stopped, q): #array, fs=8000):
        #self.playMetronomeSound()
        self.shouldCloseAudioPlayer = False
        index = 0
        #chunksize = 1024
        chunksize = int(self.original_sample_rate/self.currentFPS)
        #print("Chunk size set to:" + str(chunksize))
        #print("currentFPS is (fs):" + str(self.currentFPS))
        #print("SampleRate is (fs):" + str(self.original_sample_rate))
        #print("1/(self.original_sample_rate/chunksize):" + str(1/(self.original_sample_rate/chunksize)))
        #print("1/fps:" + str(1/(self.currentFPS)))
        plotContainer = self.getPlots()
        while not self.shouldCloseAudioPlayer:
            if self.shouldPlayAudio:
                self.currentAudioPlayerNewPosition = False
                p = pyaudio.PyAudio()
                self.currentAudioPlayerStartPosition = int(self.currentAudioPlayerStartPositionXaxis*self.original_sample_rate)
                array = self.original_sample_data[self.currentAudioPlayerStartPosition:]
                stream = p.open(format=pyaudio.paInt16, channels=len(array.shape), rate=self.original_sample_rate, output=True)
                index = 0
                chunksize = int(self.original_sample_rate/self.currentFPS)
                real_chunksize = float(self.original_sample_rate/self.currentFPS)
                #print("Chunk size set to:" + str(chunksize))
                #print("real_chunksize size set to:" + str(real_chunksize))
                #print("currentFPS is (fs):" + str(self.currentFPS))
                #print("SampleRate is (fs):" + str(self.original_sample_rate))
                #print("1/(self.original_sample_rate/chunksize):" + str(1 / (self.original_sample_rate / chunksize)))
                #print("1/fps:" + str(1 / (self.currentFPS)))

                while len(array) > index*chunksize and self.shouldPlayAudio and not self.currentAudioPlayerNewPosition:
                    for plot in plotContainer:
                        if not plotContainer[plot].isVisible:
                            continue

                        self.scatter_x_axis = plotContainer[plot].getXaxis()
                        self.scatter_y_axis = []
                        while len(self.scatter_y_axis) == 0:
                            self.scatter_y_axis = plotContainer[plot].getYaxis()
                        #QMetaObject.invokeMethod(self.parent.parent, "updateAudioPlayerLine", Qt.QueuedConnection)

                        indice_index = 0
                        #xShift = plotContainer[plot].getCurrentXShift()

                        #original_y_data = plotContainer[plot].getYaxis()
                        #original_x_data = plotContainer[plot].getXaxis()
                        if self.currentAudioPlayerStartPositionXaxis >= self.scatter_x_axis[0]:
                            tryAgain = True
                            while tryAgain:
                                try:
                                    f = interp1d(self.scatter_x_axis, self.scatter_y_axis, kind='linear')
                                    y_value_at_x = f(self.currentAudioPlayerStartPositionXaxis)
                                    if (y_value_at_x < self.parent.metronomeUnderValue and self.parent.shouldUseMetronomeUnderValue) or (y_value_at_x > self.parent.metronomeOverValue and self.parent.shouldUseMetronomeOverValue):
                                        if self.parent.shouldOnlyBeepOnCadence:
                                            real_indice = int(round(self.currentAudioPlayerStartPositionXaxis / (1 / self.currentFPS)))
                                            if ((real_indice) % self.parent.parent.DeforumationMotions.cadence) != 0:
                                                #print("Didn't play indice:" + str(real_indice))
                                                break
                                        self.playMetronomeSound()
                                        print("Beep at:" + str(self.currentAudioPlayerStartPositionXaxis))
                                    tryAgain = False
                                except Exception as e:
                                    #print("Error while dragging:" + str(e))
                                    self.scatter_x_axis = plotContainer[plot].getXaxis()
                                    self.scatter_y_axis = plotContainer[plot].getYaxis()
                                    while len(self.scatter_y_axis) != len(self.scatter_x_axis):
                                        #print("Trying to fetch graphs again.")
                                        self.scatter_y_axis = plotContainer[plot].getYaxis()
                                        self.scatter_x_axis = plotContainer[plot].getXaxis()
                                    #print("Len:" + str(len(self.scatter_y_axis[indice_index])))
                                    #print("---->" + str(self.scatter_y_axis[indice_index]))

                    write_from = int(index*real_chunksize)
                    write_to = int((index+1)*real_chunksize)
                    stream.write(array[write_from:write_to].tobytes())
                    index += 1
                    self.currentAudioPlayerStartPositionXaxis = self.currentAudioPlayerStartPositionXaxis + float(1/self.currentFPS) #float(1/(self.original_sample_rate/chunksize))

                    #self.parent.showAudioWave(shouldUpdateAll=True)
                    QMetaObject.invokeMethod(self.parent.parent, "updateAudioPlayerLine", Qt.QueuedConnection)

                stream.stop_stream()
                stream.close()
                p.terminate()
                if self.currentAudioPlayerNewPosition:
                    self.currentAudioPlayerNewPosition = False
                else:
                    self.shouldPlayAudio = False
            else:
                if self.shouldPlayAudioRememberPosition:
                    self.currentAudioPlayerStartPositionXaxis = self.startPositionAudioPlayerStartPositionXaxis
                    print("Returning to:" + str(self.currentAudioPlayerStartPositionXaxis))
                    QMetaObject.invokeMethod(self.parent.parent, "updateAudioPlayerLine", Qt.QueuedConnection)
                    self.shouldPlayAudioRememberPosition = False

                time.sleep(0.2)
        print("Closing Audio Player")
    def readWaveFile(self, filePath, downsample=None):
        #if self.original_sample_data != None:
        try:
            if not os.path.exists(filePath):
                #QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
                msgBox  = QMessageBox()
                msgBox.setText("Couldn't find the wave file belonging to this audio setting.\n\"" + str(filePath) +"\"")
                msgBox.setInformativeText("Do you want to manually find it?")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msgBox.setDefaultButton(QMessageBox.Ok)
                ret = msgBox.exec()
                if ret == QMessageBox.Ok:
                    filePath, _ = QFileDialog.getOpenFileName(self.parent.parent, "Wave file", "", "All (*.*)")
                else:
                    return -1
            self.parent.currentFilePath = filePath
            del self.original_sample_data
            self.original_sample_rate, self.original_sample_data = wavfile.read(filePath)
            self.metronome_sample_rate, self.metronome_sample_data = wavfile.read("./audio/metronome.wav")

            self.currentTotalAudioVideoFrames = int(len(self.original_sample_data)/self.original_sample_rate * self.currentFPS)
            #print("Audio is probably seconds long:" + str(len(self.original_sample_data)/self.original_sample_rate))
            #print("That is number of frames with current fps:" + str(self.currentTotalAudioVideoFrames))
            #print("Which would suggest a granularity of:" + str(int(self.currentTotalAudioVideoFrames/17)))
            self.parent.parent.ui.preview_compression_slider.setMaximum(int(self.currentTotalAudioVideoFrames/10))

            # Start the live view thread
            if self.audioplayer_t !=None:
                print("Trying to stop audio player")
                self.audioplayer_t.join()
                print("Audio player stopped")
            self.audio_player_stopped = threading.Event()
            self.audio_player_q = queue.Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK_SIZE)))
            self.audioplayer_t = threading.Thread(target=self.audioPlayer, args=(self.audio_player_stopped, self.audio_player_q))
            self.audioplayer_t.start()

            self.currentAudioPlayerStartPosition = self.original_sample_rate*30
            #self.sound(self.original_sample_data[self.original_sample_rate*30:], self.original_sample_rate)

            self.currentAudioFilePath = filePath
            self.modified_sample_data = self.original_sample_data.copy()
            self.modified_sample_time = np.arange(len(self.modified_sample_data)) / float(self.original_sample_rate)
            #Always convert wave to mono (never work in stereo with audio-synq manipulation... for now at least)
            self.modified_sample_data = self.convertToMono(self.modified_sample_data)
            if downsample != None:
                self.modified_sample_time, self.modified_sample_data =  self.downSample(self.modified_sample_data, downsample)
        except Exception as e:
            print("Error when loading audio file:" + str(e))
        return 0
    def revertToOriginal(self):
        del self.modified_sample_data
        del self.modified_sample_time
        self.modified_sample_data = self.original_sample_data.copy()
        self.modified_sample_time = np.arange(len(self.modified_sample_data)) / float(self.original_sample_rate)
        self.modified_sample_data = self.convertToMono(self.modified_sample_data)
    def setCurrentAmplitude(self, amplitude, plotName = None):
        if plotName == None:
            self.currentAmplitude = amplitude
        else:
            if plotName in self.plotDataContainer:
                self.plotDataContainer[plotName].setCurrentAmplitude(amplitude)
            else:
                print("Can't set amplitude " + str(amplitude) + " to plot with name \"" + str(plotName) + "\" because it does not exist")

    def getCurrentAmplitude(self, plotName = None):
        if plotName == None:
            return self.currentAmplitude

        else:
            if plotName in self.plotDataContainer:
                return self.plotDataContainer[plotName].getCurrentAmplitude()
            else:
                print("Can't get amplitude from plot with name \"" + str(plotName) + "\" because it does not exist")
                return None

    def getcurrentPlotMinValue(self, plotName = None):
        if plotName == None:
            currentMinVal = 9999999
            hasPlot = False
            for plot in self.plotDataContainer:
                if not self.plotDataContainer[plot].isVisible:
                    continue

                '''if plot == self.parent.strengthPlotName:
                    if not self.parent.show_strength_curve_checkbox:
                        continue
                if plot == self.parent.zoomPlotName:
                    if not self.parent.show_zoom_curve_checkbox:
                        continue'''

                plotMinVal = self.plotDataContainer[plot].getcurrentPlotMinValue()
                hasPlot = True
                if plotMinVal < currentMinVal:
                    currentMinVal = plotMinVal
            if not hasPlot:
                currentMinVal = 0
            return currentMinVal
        else:
            if plotName in self.plotDataContainer:
                return self.plotDataContainer[plotName].getcurrentPlotMinValue()
            else:
                print("Can't get plot min value from plot with name \"" + str(plotName) + "\" because it does not exist")
                return None

    def getcurrentPlotMaxValue(self, plotName = None):
        if plotName == None:
            currentMaxVal = -9999999
            hasPlot = False
            for plot in self.plotDataContainer:
                if not self.plotDataContainer[plot].isVisible:
                    continue

                '''if plot == self.parent.strengthPlotName:
                    if not self.parent.show_strength_curve_checkbox:
                        continue
                if plot == self.parent.zoomPlotName:
                    if not self.parent.show_zoom_curve_checkbox:
                        continue'''

                plotMaxVal = self.plotDataContainer[plot].getcurrentPlotMaxValue()
                hasPlot = True
                if plotMaxVal > currentMaxVal:
                    currentMaxVal = plotMaxVal
            if not hasPlot:
                currentMaxVal = 1
            return currentMaxVal
        else:
            if plotName in self.plotDataContainer:
                return self.plotDataContainer[plotName].getcurrentPlotMaxValue()
            else:
                print("Can't get plot max value from plot with name \"" + str(plotName) + "\" because it does not exist")
                return None

    def setCurrentShift(self, shift, plotName = None):
        if plotName == None:
            self.currentShift = shift
        else:
            if plotName in self.plotDataContainer:
                self.plotDataContainer[plotName].setCurrentShift(shift)
            else:
                print("Can't set shift " + str(shift) + " to plot with name \"" + str(plotName) + "\" because it does not exist")

    def getCurrentShift(self, plotName = None):
        if plotName == None:
            return self.currentShift
        else:
            if plotName in self.plotDataContainer:
                return self.plotDataContainer[plotName].getCurrentShift()
            else:
                print("Can't get shift from plot with name \"" + str(plotName) + "\" because it does not exist")
                return None


    def getYAxisRange(self, plotName):
        if plotName in self.plotDataContainer:
            return self.plotDataContainer[plotName].getYAxisRange()
        else:
            print("Can't get plot Y Range from plot with name \"" + str(plotName) + "\" because it does not exist")
            return None
    def setYAxisRange(self, plotName, plotYRange):
        if plotName in self.plotDataContainer:
            self.plotDataContainer[plotName].setYAxisRange(plotYRange)
        else:
            print("Can't set plot Y Range on plot with name \"" + str(plotName) + "\" because it does not exist")

    def getOriginalSampleData(self):
        return self.original_sample_data
    def getOriginalSampleRate(self):
        return self.original_sample_rate

    def getXaxis(self):
        return self.modified_sample_time
    def getYaxis(self):
        return self.modified_sample_data

    def getAudioDataLen(self):
        return len(self.modified_sample_time)

    def getModifiedSampleData(self):
        return self.modified_sample_data

    def convertToMono(self, sample_data):
        if sample_data.ndim == 2:  # Check if stereo
            sample_data = sample_data.mean(axis=1)  # Convert to mono
        return sample_data

    def setCurrentFPS(self, fps):
        self.currentFPS = fps
        self.chunk_duration_ms = 1000 / self.currentFPS
        self.waveIndexPerFrame = float(self.chunk_duration_ms / (self.modified_sample_time[1] * 1000))
        self.currentTotalAudioVideoFrames = int(len(self.original_sample_data)/self.original_sample_rate * self.currentFPS)
        if self.currentTotalAudioVideoFrames > self.parent.parent.total_number_of_frames_generated:
        #    self.parent.parent.ui.movie_slider.setMaximum(int(self.parent.parent.total_number_of_frames_generated / self.VideoImageContainer.getPreviewCompression()))
        #else:
            self.parent.parent.ui.movie_slider.setMaximum(int(self.currentTotalAudioVideoFrames / self.parent.parent.VideoImageContainer.getPreviewCompression()))

    def getCurrentFPS(self):
        return self.currentFPS

    def downSample(self, sample_data, max_points = 100000):
        downsampling_factor = max(1, len(sample_data) // max_points)
        # Apply downsampling by taking every nth sample
        downsampled_data = sample_data[::downsampling_factor]
        downsampled_times = np.arange(len(downsampled_data)) / float(self.original_sample_rate) * downsampling_factor
        return downsampled_times, downsampled_data
        #self.modified_sample_time = downsampled_times
        #self.modified_sample_data = downsampled_data

    def downSampleExisting(self, max_points = 100000):
        downsampling_factor = max(1, len(self.modified_sample_data) // max_points)
        # Apply downsampling by taking every nth sample
        downsampled_data = self.modified_sample_data[::downsampling_factor]
        downsampled_times = np.arange(len(downsampled_data)) / float(self.original_sample_rate) * downsampling_factor
        self.modified_sample_time = downsampled_times
        self.modified_sample_data = downsampled_data

        self.waveIndexPerFrame = float(self.chunk_duration_ms / (downsampled_times[1] * 1000))
    def getPlot(self, plotName):
        if plotName in self.plotDataContainer:
            return self.plotDataContainer[plotName]
        else:
            print("A plot with name \"" + plotName + "\" doesn't exist and can't be returned.")
        return None
    def getPlots(self):
        return self.plotDataContainer
    def isThereAnySelection(self):
        plotContainer = self.getPlots()
        for plot in plotContainer:
            indices = plotContainer[plot].getSelectedIndices()
            if len(indices) > 0:
                return True
        return False

    def addPlot(self, plotName, shouldUseDownsampledData = False, pen=None, brush=None):
        if shouldUseDownsampledData:
            newPlot = PlotDataContainer(self, plotName, sample_rate = None, sample_data = self.modified_sample_data, pen=pen, brush=brush)
        else:
            newPlot = PlotDataContainer(self, plotName, pen=pen, brush=brush)
        if plotName not in self.plotDataContainer:
            self.plotDataContainer[plotName] = newPlot
            #print("Added plot \"" + plotName + "\"")
        else:
            print("A plot with name \"" + plotName + "\" already exists and must first be deleted or renamed to be free to use again.")
    def removePlot(self, plotName):
        index = 0
        if plotName in self.plotDataContainer:
            del self.plotDataContainer[plotName]
            #print("Removed plot \"" + plotName + "\"")
        else:
            print("A plot with name \"" + plotName + "\" doesn't exist and can't be deleted.")

    def getwaveIndexPerFrame(self):
        return self.waveIndexPerFrame

    def setAmplitudeRangeZeroOne(self, minVal = None, maxVal = None, plotName = None):
        #Make it go from 0 to 1
        #self.modified_sample_data = self.original_sample_data.copy()
        if plotName !=None:
            self.currentMinValue = self.getcurrentPlotMinValue(plotName)
            self.currentMaxValue = self.getcurrentPlotMaxValue(plotName)
        else:
            for plot in self.plotDataContainer:
                currentPlot = self.plotDataContainer[plot] #self.audioDataContainer.getPlot(self.strengthPlotName)
                currentPlot.setAmplitudeAndShift()

            self.currentMinValue = self.getcurrentPlotMinValue()
            self.currentMaxValue = self.getcurrentPlotMaxValue()
            if minVal != None:
                self.currentMinValue = minVal
            if maxVal != None:
                self.currentMaxValue = maxVal

        if self.original_sample_data.dtype == np.int16:
            self.modified_sample_data = self.modified_sample_data / 32768.0  # Convert 16-bit integers to -1 to 1 range
        elif self.original_sample_data.dtype == np.int32:
            self.modified_sample_data = self.modified_sample_data / 2147483648.0
        self.modified_sample_data = (self.modified_sample_data + 1) / 2
        rangeModifier = self.currentMaxValue-self.currentMinValue
        self.modified_sample_data = self.modified_sample_data * rangeModifier + self.currentMinValue #0.75

    def setAmplitudeRangeZeroOne(self, minVal = None, maxVal = None, plotName = None):
        #Make it go from 0 to 1
        #self.modified_sample_data = self.original_sample_data.copy()
        if plotName !=None:
            self.currentMinValue = self.getcurrentPlotMinValue(plotName)
            self.currentMaxValue = self.getcurrentPlotMaxValue(plotName)
        else:
            for plot in self.plotDataContainer:
                currentPlot = self.plotDataContainer[plot] #self.audioDataContainer.getPlot(self.strengthPlotName)
                currentPlot.setAmplitudeAndShift()

            self.currentMinValue = self.getcurrentPlotMinValue()
            self.currentMaxValue = self.getcurrentPlotMaxValue()
            if minVal != None:
                self.currentMinValue = minVal
            if maxVal != None:
                self.currentMaxValue = maxVal

        if self.original_sample_data.dtype == np.int16:
            self.modified_sample_data = self.modified_sample_data / 32768.0  # Convert 16-bit integers to -1 to 1 range
        elif self.original_sample_data.dtype == np.int32:
            self.modified_sample_data = self.modified_sample_data / 2147483648.0
        self.modified_sample_data = (self.modified_sample_data + 1) / 2
        rangeModifier = self.currentMaxValue-self.currentMinValue
        self.modified_sample_data = self.modified_sample_data * rangeModifier + self.currentMinValue #0.75



class Audio_Wave_View_Box(pg.ViewBox):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        #emptyarg = ()
        # doh = *blaha
        #super().__init__(*emptyarg, **kwargs)
        #super().__init__(*args, **kwargs)
        self.setMouseMode(self.PanMode)  # Default mouse mode to panning
        self.dragging = False
        self.currentAudioStartTimeInView = self.viewRange()[0][0]
        self.currentAudioStartEndInView = self.viewRange()[0][1]
        self.draggingStartPos = 0
        self.initialXRange = self.viewRange()[0]
        self.initialYRange = self.viewRange()[1]
        self.current_selected_indices = []
        self.scatter_current_brushes = []
        self.scatter_current_pens = []
        self.dragPoint = None
        self.dragIndicesStarted = False
        self.currentDragIndicePlotY = None
        self.currentDragIndicePlotX = None
        self.currentDragPlot = None
        self.scatter_x_axis = []
        self.scatter_y_axis= []
        self.current_scatterPlot_audioFrameLeft = None
        self.current_scatterPlot_audioFrameRight = None
        self.setMenuEnabled(False)
        self.singlePoint = pg.ScatterPlotItem()
        self.hasAddedSinglePoint = False

        #print("x-pos-time:" + str(self.viewRange()[0][0]))
    def setAudioRange(self, newLeft, newRight):
        if not self.dragging:
            self.setXRange(newLeft, newRight, padding=0)
        else:
            #print("newLeft:" + str(newLeft) + " --- newRight:" + str(newRight))
            self.currentAudioStartTimeInView = newLeft #range[0] + frameStep
            self.currentAudioStartEndInView = newRight #range[1] + frameStep
            self.initialXRange = [newLeft, newRight]

    def calculateSelectionRect(self, start, end):
        """Calculate the selection rectangle from start and end points."""
        path = QPainterPath()
        path.addRect(start.x(), start.y(), end.x() - start.x(), end.y() - start.y())
        return path

    def findPointsInRect(self, rect, plot): #x_axis, y_axis,):
        # Make current selection white again
        """Find indices of points within the selection rectangle."""
        #if len(self.current_selected_indices) > 0:
        #    self.revert_points_to_original_colors()
        selected_indices = []
        selected_indices_original = []
        x_axis = plot.getXaxis()
        y_axis = plot.getYaxis()
        for n in range(0, len(x_axis)):
            xPos = x_axis[n]
            yPos = y_axis[n]
            if rect.contains(QPointF(xPos, yPos)):
                selected_indices.append(n)
                current_fps = self.parent.audioDataContainer.currentFPS
                corrected_x_pos = (xPos + 0.2 / current_fps) - ((xPos + 0.2 / current_fps) % (1 / current_fps))
                relative_indice = int((xPos + 0.2 / current_fps) / (1 / current_fps)) #corrected_x_pos / (1 / current_fps))
                xShift = plot.getCurrentXShift()
                #if xShift < 0:
                relative_indice = relative_indice - xShift
                #print("Indice:" + str(n) + " -- is really indice:" + str(relative_indice))
                selected_indices_original.append(relative_indice)

        self.current_selected_indices = selected_indices
        self.current_selected_indices_original = selected_indices_original
        return selected_indices, selected_indices_original

    def copyPointValues(self):
        plotContainer = self.parent.audioDataContainer.getPlots()
        y_axis = plotContainer[self.parent.selectedPlot].getYaxis()
        x_axis = plotContainer[self.parent.selectedPlot].getXaxis()
        selected_points = sorted(plotContainer[self.parent.selectedPlot].getSelectedIndices())
        selected_points_original = sorted(plotContainer[self.parent.selectedPlot].getSelectedIndicesOriginal())
        self.parent.copyBuffer = np.array(plotContainer[self.parent.selectedPlot].chunk_amplitudes)[selected_points_original] #y_axis[selected_points]
        self.parent.copyBuffer_x = selected_points
        self.parent.copyBuffer_modifiers =  plotContainer[self.parent.selectedPlot].chunk_modified_sample_data_amp_strength_modifiers[selected_points_original]
        self.parent.copyBuffer_x_original = selected_points_original

        pass

    def pastePointValues(self):
        plotContainer = self.parent.audioDataContainer.getPlots()
        y_axis = plotContainer[self.parent.selectedPlot].getYaxis_chunk()

    def change_points_colors(self, selected_indices, plot=None, hover=False, affectCopyAlso = False, selectedIndicesOriginal = None, selectAll = 0):
        # Update colors for selected indices
        if plot == None:
            plotContainer = self.parent.audioDataContainer.getPlots()
            for plot in plotContainer:
                plotContainer[plot].setSelectedIndices(selected_indices, affectCopyAlso=affectCopyAlso, selectedIndicesOriginal = selectedIndicesOriginal)
                self.doScatterPlotFromPlot(plotContainer[plot])
        else:
            if not hover:
                plot.setSelectedIndices(selected_indices, affectCopyAlso=affectCopyAlso, selectedIndicesOriginal = selectedIndicesOriginal, selectAll = selectAll)
            else:
                #if len(selected_indices) > 0:
                #    selected_indices = selected_indices + plot.getCurrentXShift()
                plot.setHoverIndice(selected_indices)
            self.doScatterPlotFromPlot(plot)

    def doScatterPlotFromPlot(self, plot, audioFrameLeft=None, audioFrameRight=None, scatter_pen = None, scatter_brush = None):
        if audioFrameLeft != None:
            self.current_scatterPlot_audioFrameLeft = audioFrameLeft
        else:
            if self.current_scatterPlot_audioFrameLeft == None:
                self.current_scatterPlot_audioFrameLeft = 0

        if audioFrameRight != None:
            self.current_scatterPlot_audioFrameRight = audioFrameRight
        else:
            if self.current_scatterPlot_audioFrameRight == None:
                self.current_scatterPlot_audioFrameRight = plot.getPlotDataLen()

        if self.current_scatterPlot_audioFrameLeft == 1:
            pass
        self.scatter_x_axis = plot.getXaxis()
        self.scatter_y_axis = plot.getYaxis()
        currentScatter = plot.getScatter()
        currentLines = plot.getLines()

        scatter_pen = plot.getCurrentScatterPen() #getOriginalScatterPen()
        scatter_line_pen_color = plot.getCurrentScatterLinePenColor()
        scatter_brush = plot.getCurrentScatterBrush()

        xShift = plot.getCurrentXShift()
        relative_shift = self.current_scatterPlot_audioFrameLeft - xShift

        #relative_scatterPlot_audioFrameLeft = 0 #TESTING TESTING

        if len(self.scatter_x_axis) != len(scatter_pen):
            pass

        #currentScatter.setData(self.scatter_x_axis[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], self.scatter_y_axis[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], symbol='o', size=6, brush=scatter_brush[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], hoverable=True)
        #currentScatter.setPen(scatter_pen[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight])
        #Testing Testing
        currentScatter.setData(self.scatter_x_axis[0:len(self.scatter_x_axis)], self.scatter_y_axis[0:len(self.scatter_x_axis)], symbol='o', size=6, brush=scatter_brush[0:len(self.scatter_x_axis)], hoverable=True)
        currentScatter.setPen(scatter_pen[0:len(self.scatter_x_axis)])


        # Always draw lines connecting all points
        #currentLines.setData(self.scatter_x_axis[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], self.scatter_y_axis[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], pen=scatter_line_pen_color)
        #currentLines.setCurveClickable(True) #TESTING TESTING
        #Testing Testing
        currentLines.setData(self.scatter_x_axis[0:len(self.scatter_x_axis)], self.scatter_y_axis[0:len(self.scatter_x_axis)], pen=scatter_line_pen_color)
        currentLines.setCurveClickable(True) #TESTING TESTING

        #pg.ScatterPlotItem.
        self.addItem(currentScatter)
        self.addItem(currentLines)

    def addSinglePoint(self, plot, indice_index, value, shouldSet = False):

        if self.hasAddedSinglePoint:
            self.removeItem(self.singlePoint)
            self.hasAddedSinglePoint = False

        current_fps = self.parent.audioDataContainer.currentFPS
        x_pos = indice_index * (1 / current_fps)
        y_pos = value #plot.calculateChunkAmplitudeFromCurrentValue(value)
        pen = pg.mkPen(color=(0, 255, 0, 255), width=2)
        brush = pg.mkBrush(color=(0, 255, 0, 255))
        self.singlePoint.setData([x_pos], [y_pos], symbol='o', size=6, brush=[brush])
        self.singlePoint.setPen(pen)
        self.addItem(self.singlePoint)
        self.hasAddedSinglePoint = True

    def removeSinglePoint(self, plot):
        #kalle = self.allChildren()
        if  self.hasAddedSinglePoint:
            #print("Removing singlePoint")
            self.removeItem(self.singlePoint)
            self.hasAddedSinglePoint = False

    def isMousePositionOnScatterPoint(self, mousePointHotSpot, plot):
        x_axis = plot.getXaxis()
        y_axis = plot.getYaxis()
        for n in range(0, len(x_axis)):
            xPos = x_axis[n]
            yPos = y_axis[n]
            if mousePointHotSpot.contains(QPointF(xPos, yPos)):
                print("You hit a node")

    '''def mouseClickEvent(self, event):
        if event.type() == QEvent.MouseButtonPress:
            if event.button() == Qt.LeftButton:
                print("Mouse left down")
            if event.button() == Qt.RightButton:
                print("Mouse right down")'''

    def mousePressEventAudioMenu(self, event, action, popMenu):
        if action == "go to audio needle":
            QMetaObject.invokeMethod(self.parent.parent, "updateAudioPlayerLine", Qt.QueuedConnection)
        #print("Action:" + str(action))

        popMenu.close()
    def mouseClickEvent(self, ev):
        if ev.button() == Qt.LeftButton:
            if self.parent.graphWidget.singlePointIsShowing and self.parent.setShiftKeyDown and self.parent.graphWidget.singlePointIndex != -1:
                #print("Setting value:" + str(self.parent.graphWidget.singlePointValue))
                #print("Setting value On Index:" + str(self.parent.graphWidget.singlePointIndex))
                plotContainer = self.parent.audioDataContainer.getPlots()
                plotContainer[self.parent.selectedPlot].chunk_amplitudes[self.parent.graphWidget.singlePointIndex] = plotContainer[self.parent.selectedPlot].calculateChunkAmplitudeFromCurrentValue(self.parent.graphWidget.singlePointValue)
                plotContainer[self.parent.selectedPlot].chunk_modified_sample_data_amp_strength_modifiers[self.parent.graphWidget.singlePointIndex] = 0
                plotContainer[self.parent.selectedPlot].removeFromRemovedVertices([self.parent.graphWidget.singlePointIndex])
                plotContainer[self.parent.selectedPlot].setAmplitudeAndShift(shouldChangeROIminmax=True)
                QMetaObject.invokeMethod(self.parent.parent, "showAudioWave", Qt.QueuedConnection)
                if plotContainer[self.parent.selectedPlot].should_synq_with_mediator:
                    self.parent.sendGraphToMediator(self.parent.selectedPlot, True)
            else:
                pos = self.mapToView(ev.pos())
                #print("Clicked at pos:" + str(pos))
                current_fps = self.parent.audioDataContainer.currentFPS
                self.parent.audioDataContainer.currentAudioPlayerStartPositionXaxis = pos.x() - (pos.x() % (1/current_fps))
                self.parent.audioDataContainer.startPositionAudioPlayerStartPositionXaxis = self.parent.audioDataContainer.currentAudioPlayerStartPositionXaxis
                #print("Audio needle got position:" + str(self.parent.audioDataContainer.currentAudioPlayerStartPositionXaxis))
                #closest_needle_position = self.parent.audioDataContainer.currentAudioPlayerStartPositionXaxis - (self.parent.audioDataContainer.currentAudioPlayerStartPositionXaxis % (1/current_fps))
                #print("Audio needle current pos:"  + str(self.parent.audioDataContainer.currentAudioPlayerStartPositionXaxis))
                self.parent.audioDataContainer.currentAudioPlayerNewPosition = True
                QMetaObject.invokeMethod(self.parent.parent, "updateAudioPlayerLine", Qt.QueuedConnection)
                #self.parent.showAudioWave(shouldUpdateAll=False)

        if ev.button() == Qt.RightButton:
            #print("!Mouse was clicked!")
            popMenu = self.parent.parent.popMenu_prompt1
            if popMenu != None:
                normal_pos = ev.pos()
                scene_pos = ev.scenePos()
                screen_pos = ev.screenPos()
                mapped_pos =  self.mapToView(scene_pos) #self.mapToGlobal(ev.pos())
                #menuPosition = mapped_pos.toPoint()
                menuPosition = QPoint(screen_pos[0], screen_pos[1])


                # print("Show context menu")
                popMenu.clear()

                containerWidget = QWidget()
                containerLayout = QVBoxLayout()
                containerLayout.setSpacing(0)
                containerLayout.setObjectName(u"verticalLayout_rsdffdsf")
                containerLayout.setContentsMargins(0, 0, 0, 0)
                popMenu.setStyleSheet(u"QMenu {border: 0px;}")
                morphPromptMenuLabelStyle = u"QLabel {\n    background-color: rgb(220,220,220); /* Matching the tab's base color */\n     color: rgb(0,0,0);\n    border-left: 0px solid rgb(220,220,220);\n    border-right: 0px solid rgb(220,220,220);\n    border-top: 0px solid rgb(220,220,220);\n    border-bottom: 2px solid rgb(220,220,220);\n	border-radius:0;\n    padding:0;\n}\n\nQLabel:hover {\n    background-color: rgb(150,150,200); /* Matching the tab's base color */\n    color: rgb(0, 100, 0); /* Matching the tab's base color */\n    color: rgb(0,0,0);\n	border:0\n}\n\nQLabel:pressed {\n    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n	border:0\n}"
                morphPromptMenuStandardLabelStyleFinal = u"QLabel {\n    background-color: rgb(50,50,50); /* Matching the tab's base color */\n     color: rgb(220,220,220);\n    border-left: 0px solid rgb(50,50,50);\n    border-right: 0px solid rgb(50,50,50);\n    border-top: 0px solid rgb(50,50,50);\n    border-bottom: 2px solid rgb(180,140,180);\n	border-radius:0;\n    padding:0;\n}\n\nQLabel:hover {\n    background-color: rgb(80,80,140); /* Matching the tab's base color */\n    color: rgb(0, 100, 0); /* Matching the tab's base color */\n    color: rgb(0,0,0);\n	border:0\n}\n\nQLabel:pressed {\n    background-color: rgb(80,80,140); /* Similar to the selected tab color */\n	border:0\n}"
                morphPromptMenuStandardLabelStyle = u"QLabel {\n    background-color: rgb(50,50,50); /* Matching the tab's base color */\n     color: rgb(220,220,220);\n    border-left: 0px solid rgb(50,50,50);\n    border-right: 0px solid rgb(50,50,50);\n    border-top: 0px solid rgb(50,50,50);\n    border-bottom: 2px solid rgb(50,50,50);\n	border-radius:0;\n    padding:0;\n}\n\nQLabel:hover {\n    background-color: rgb(80,80,140); /* Matching the tab's base color */\n    color: rgb(0, 100, 0); /* Matching the tab's base color */\n    color: rgb(0,0,0);\n	border:0\n}\n\nQLabel:pressed {\n    background-color: rgb(80,80,140); /* Similar to the selected tab color */\n	border:0\n}"
                # First add cut and paste in the menu
                standardtextedititems = ["Cut", "Copy", "Paste", "go to audio needle"]
                for standarditem in standardtextedititems:
                    self.anItem = QLabel()
                    self.anItem.setText(standarditem)
                    self.anItem.setObjectName(u"morph_standard_" + standarditem)
                    self.anItem.setGeometry(QRect(0, 0, 100, 40))
                    font12 = QFont()
                    font12.setPointSize(11)
                    self.anItem.setFont(font12)
                    if standarditem != "Paste":
                        self.anItem.setStyleSheet(morphPromptMenuStandardLabelStyle)
                    else:
                        self.anItem.setStyleSheet(morphPromptMenuStandardLabelStyleFinal)

                    self.anItem.mousePressEvent = lambda event, item=standarditem, popMenu=popMenu: self.mousePressEventAudioMenu(event, item, popMenu)
                    containerLayout.addWidget(self.anItem)

                containerWidget.setLayout(containerLayout)
                # Create a scroll area and add the container widget to it
                scrollArea = QScrollArea()
                scrollArea.setStyleSheet("QScrollArea {border: 0px;}")
                scrollArea.setWidgetResizable(True)
                scrollArea.setWidget(containerWidget)
                scrollArea.setMinimumWidth(200)
                scrollArea.setMaximumHeight(600)
                # Create a QWidgetAction and set the scroll area as its default widget
                scrollWidgetAction = QWidgetAction(popMenu)
                scrollWidgetAction.setDefaultWidget(scrollArea)
                popMenu.addAction(scrollWidgetAction)

                popMenu.popup(menuPosition)
    def mouseDragEvent(self, ev, axis=None):
        if ev.button() == Qt.LeftButton:
            ev.accept()
            if ev.isStart():
                # Capture the initial y-axis range to restore it after panning
                self.dragging = True
                #print("Xrange:" + str(self.viewRange()[0]))
                #print("Yrange:" + str(self.viewRange()[1]))
                self.initialXRange = self.viewRange()[0]
                self.initialYRange = self.viewRange()[1]
                self.draggingStartPos = ev.buttonDownPos()[0]

                plotContainer = self.parent.audioDataContainer.getPlots()
                for plot in plotContainer:
                    if not plotContainer[plot].isVisible or not plotContainer[plot].isEditable:
                        continue
                    pos = self.mapToView(ev.buttonDownPos(Qt.LeftButton)) # ev.buttonDownPos()
                    scatter = plotContainer[plot].getScatter()
                    pts = scatter.pointsAt(pos)
                    if len(pts) != 0:
                        self.dragIndicesStarted = True
                        self.dragPoint = pts[0]

                        #arne = self.dragPoint.pos()
                        x, y = self.dragPoint.pos()
                        original_y_data = plotContainer[plot].getYaxis()
                        original_x_data = plotContainer[plot].getXaxis()

                        #This below method to calculate the plot index seems unnecessary
                        #index = next((i for i, (px, py) in enumerate(zip(original_x_data, original_y_data)) if px == x and py == y), None)
                        #And can be replaced with below:
                        relativeIndexSelection = self.dragPoint.index()
                        index = self.current_scatterPlot_audioFrameLeft + relativeIndexSelection
                        index = relativeIndexSelection  # TESTING TESTING
                        self.currentDragIndiceIndex = index
                        self.currentDragPlot = plotContainer[plot]
                        self.currentDragIndicePlotY = original_y_data
                        self.currentDragIndicePlotX = original_x_data
                        '''xShift = self.currentDragPlot.getCurrentXShift()
                        if xShift < 0:
                            index = self.currentDragIndiceIndex - xShift'''

                        xShift = self.currentDragPlot.getCurrentXShift()
                        relativeIndexSelection = self.dragPoint.index()
                        howMuchIsNotVisible = self.current_scatterPlot_audioFrameLeft - xShift
                        #index = relativeIndexSelection #self.viewBox.current_scatterPlot_audioFrameLeft + relativeIndexSelection

                        index = relativeIndexSelection  # TESTING TESTING
                        '''if xShift < 0:
                            index = index + self.current_scatterPlot_audioFrameLeft - xShift
                        elif howMuchIsNotVisible > 0:
                            index = index + howMuchIsNotVisible
                        else:
                            index = relativeIndexSelection'''

                        self.currentDragIndiceIndex = index
                        #TESTING
                        current_fps = self.parent.audioDataContainer.currentFPS
                        mousePoint = pos
                        corrected_x_pos = (mousePoint.x() + 0.2 / current_fps) - ((mousePoint.x() + 0.2 / current_fps) % (1 / current_fps))
                        #print("ORG-X-DRAG Position Corrected:" + str(mousePoint.x()))
                        #print("X-DRAG Position Corrected:" + str(corrected_x_pos))
                        relative_indice = int((plotContainer[plot].modified_sample_time_amp_strength[index] + 0.2 / current_fps) / (1 / current_fps)) #int(corrected_x_pos / (1 / current_fps))
                        xShift = self.currentDragPlot.getCurrentXShift()
                        relative_indice = relative_indice - xShift
                        '''if xShift < 0:
                            relative_indice = relative_indice + self.current_scatterPlot_audioFrameLeft - xShift
                        elif howMuchIsNotVisible > 0:
                            relative_indice = relative_indice + howMuchIsNotVisible
                        else:
                            relative_indice = relativeIndexSelection'''

                        #print("X-DRAG relative_indice:" + str(relative_indice))
                        self.currentDragIndiceIndexOriginalPosition = relative_indice

                        self.currentIndixceStartValue =  str('%.2f' % float(self.currentDragIndicePlotY[index]))
                        #print("Check if indice " + str(self.currentDragIndiceIndex) + " is already selected.")
                        self.isIndexAlreadySelected = self.currentDragPlot.isIndexSelected(self.currentDragIndiceIndex)
                        if not self.isIndexAlreadySelected:
                            for plot in plotContainer:
                                if plotContainer[plot].isVisible:
                                    plotContainer[plot].emptySelectedIndices()
                                    self.change_points_colors([], plotContainer[plot])
                                #plotContainer[plot].setAmplitudeAndShift(shouldChangeROIminmax=True)
                                #self.parent.showAudioWave(shouldUpdateAll=True)


            elif ev.isFinish():
                self.dragging = False
                if self.dragIndicesStarted:
                    self.dragIndicesStarted = False
                    self.parent.graphWidget.setLabel('bottom', 'Time', units='s')
                    #print("finished")
                    plotContainer = self.parent.audioDataContainer.getPlots()
                    for plot in plotContainer:
                        if not plotContainer[plot].isEditable:
                            continue

                        currentPlot = plotContainer[plot]
                        currentPlot.setAmplitudeAndShift(shouldChangeROIminmax=True)
                        self.parent.showAudioWave(shouldUpdateAll=True)
                        if currentPlot.should_synq_with_mediator:
                            self.parent.sendGraphToMediator(plot, True)

                else:
                    if len(self.scatter_y_axis) != 0:
                        # Compute the drag selection area
                        #drag_start = self.mapSceneToView(ev.buttonDownPos(Qt.RightButton))
                        #drag_end = self.mapSceneToView(ev.pos())

                        drag_start = self.mapToView(ev.buttonDownPos(Qt.LeftButton))
                        drag_end = self.mapToView(ev.pos())

                        drag_rect = self.calculateSelectionRect(drag_start, drag_end)

                        plotContainer = self.parent.audioDataContainer.getPlots()
                        for plot in plotContainer:
                            if not plotContainer[plot].isVisible or not plotContainer[plot].isEditable:
                                continue

                            #plot.sigClicked.connect(self.clicked)
                            selected_indices, selected_indices_original = self.findPointsInRect(drag_rect, plotContainer[plot]) #self.scatter_x_axis, self.scatter_y_axis)
                            self.change_points_colors(selected_indices, plotContainer[plot], selectedIndicesOriginal = selected_indices_original)

                    self.rbScaleBox.hide()  # Hide the selection box
            else:
                # Update the scale box visually during the drag
                if self.dragIndicesStarted:
                    viewPos = self.mapToView(ev.pos())
                    #currPosX = viewPos.x()
                    currPosY = viewPos.y()
                    coord_display_string = "Original Value:" + str('%.2f' % float(self.currentIndixceStartValue)) + " -- Current Value:" + str('%.2f' % float(currPosY) + " -- Time")
                    self.parent.graphWidget.setLabel('bottom', coord_display_string, units='s')

                    #xShift = self.currentDragPlot.getCurrentXShift()
                    #if (xShift) < 0:
                    #    dragDistance = currPosY - self.currentDragIndicePlotY[self.currentDragIndiceIndex - xShift]
                    #else:
                    dragDistance = currPosY - self.currentDragIndicePlotY[self.currentDragIndiceIndex]

                    #print("Dragging Indice index:" + str(self.currentDragIndiceIndex)) #TESTING TESTING
                    self.currentDragPlot.setIndiceDragValue(self.currentDragIndiceIndex, currPosY, dragDistance)

                    scatter_brush = self.currentDragPlot.getCurrentScatterBrush()
                    scatter_pen = self.currentDragPlot.getCurrentScatterPen()  # getOriginalScatterPen()


                    #scatter = self.currentDragPlot.getScatter()
                    currentScatter = self.currentDragPlot.getScatter()

                    self.currentDragPlot.setNewIndicesMultiplierValue(self.currentDragIndiceIndex, dragDistance, self.currentDragIndiceIndexOriginalPosition)

                    xShift = self.currentDragPlot.getCurrentXShift()
                    relative_shift = self.current_scatterPlot_audioFrameLeft - xShift
                    if (relative_shift) > 0:
                        relative_scatterPlot_audioFrameLeft = relative_shift
                        relative_scatterPlot_audioFrameRight = self.current_scatterPlot_audioFrameRight + relative_shift
                    else:
                        relative_scatterPlot_audioFrameLeft = 0
                        relative_scatterPlot_audioFrameRight = self.current_scatterPlot_audioFrameRight

                    relative_scatterPlot_audioFrameLeft = 0 #TESTING TESTING
                    self.scatter_x_axis = self.currentDragPlot.getXaxis()
                    self.scatter_y_axis = self.currentDragPlot.getYaxis()
                    currentScatter.setData(self.scatter_x_axis[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], self.scatter_y_axis[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], symbol='o', size=6, brush=scatter_brush[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], hoverable=True)
                    currentScatter.setPen(scatter_pen[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight])
                    # Always draw lines connecting all points
                    scatter_line_pen_color = self.currentDragPlot.getCurrentScatterLinePenColor()
                    currentLines = self.currentDragPlot.getLines()
                    currentLines.setData(self.scatter_x_axis[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], self.scatter_y_axis[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], pen=scatter_line_pen_color)

                    if self.isIndexAlreadySelected:
                        plotContainer = self.parent.audioDataContainer.getPlots()
                        for plot in plotContainer:
                            if not plotContainer[plot].isVisible or not plotContainer[plot].isEditable:
                                continue

                            if plotContainer[plot] != self.currentDragPlot:
                                plotContainer[plot].setIndiceDragValue(None, None, dragDistance)
                                scatter_brush = plotContainer[plot].getCurrentScatterBrush()
                                scatter_pen = plotContainer[plot].getCurrentScatterPen()  # getOriginalScatterPen()
                                #scatter = plotContainer[plot].getScatter()
                                currentScatter = plotContainer[plot].getScatter()
                                plotContainer[plot].setNewIndicesMultiplierValue(None, dragDistance, None)

                                xShift = plotContainer[plot].getCurrentXShift()
                                relative_shift = self.current_scatterPlot_audioFrameLeft - xShift
                                if (relative_shift) > 0:
                                    relative_scatterPlot_audioFrameLeft = relative_shift
                                    relative_scatterPlot_audioFrameRight = self.current_scatterPlot_audioFrameRight + relative_shift
                                else:
                                    relative_scatterPlot_audioFrameLeft = 0
                                    relative_scatterPlot_audioFrameRight = self.current_scatterPlot_audioFrameRight

                                relative_scatterPlot_audioFrameLeft = 0  # TESTING TESTING
                                self.scatter_x_axis = plotContainer[plot].getXaxis()
                                self.scatter_y_axis = plotContainer[plot].getYaxis()
                                currentScatter.setData(self.scatter_x_axis[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], self.scatter_y_axis[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], symbol='o', size=6, brush=scatter_brush[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], hoverable=True)
                                currentScatter.setPen(scatter_pen[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight])
                                # Always draw lines connecting all points
                                scatter_line_pen_color = plotContainer[plot].getCurrentScatterLinePenColor()
                                currentLines = plotContainer[plot].getLines()
                                currentLines.setData(self.scatter_x_axis[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], self.scatter_y_axis[relative_scatterPlot_audioFrameLeft:relative_scatterPlot_audioFrameRight], pen=scatter_line_pen_color)

                    self.setYRange(self.initialYRange[0], self.initialYRange[1], padding=0)
                    self.setXRange(self.initialXRange[0], self.initialXRange[1], padding=0)
                else:
                    self.updateScaleBox(ev.buttonDownPos(), ev.pos())



class CustomPlotWidget(pg.PlotWidget):
    def __init__(self, *args, **kwargs):
        self.parent = args[0]
        kwargs['viewBox'] = Audio_Wave_View_Box(self.parent)
        emptyarg = ()
        super().__init__(*emptyarg, **kwargs)
        self.viewBox = kwargs['viewBox']
        self.showAxis('left', False)
        self.IndiceIsSelected = {}
        self.scene().sigMouseMoved.connect(self.mouseMoved)
        self.scene().sigMouseClicked.connect(self.MouseClicked)
        self.currentZoom = 1
        self.singlePointIsShowing = False
        self.singlePointIndex = -1
        self.singlePointValue = 0

        #self.viewBox.setMouseMode(self.viewBox.RectMode)
        # Hide the left axis
    #def doLinePlot(self, x_axis, y_axis, audioFrameLeft,audioFrameRight, pen):
    #    self.plot(x_axis[audioFrameLeft:audioFrameRight], y_axis[audioFrameLeft:audioFrameRight], pen=pen)

    #self.graphWidget.doLinePlot(self.audioData.modified_sample_time, self.audioData.modified_sample_data, 0, len(self.audioData.modified_sample_time), pg.mkPen(color=QColor(255, 255, 255, self.audioData.waveAlpha)))
    def wheelEvent(self, ev):
        if self.parent.setAltKeyDown:
            self.currentZoom = self.parent.parent.VideoImageContainer.getPreviewCompression()
            pos = ev.position()
            if self.sceneBoundingRect().contains(pos):
                old_left_frame = self.currentZoom * self.parent.parent.ui.movie_slider.value()
                old_right_frame = old_left_frame + self.currentZoom * self.parent.parent.currentlyShownMovieFrames
                old_total_shown_frames = old_right_frame - old_left_frame
                if ev.angleDelta().x() > 0:
                    if self.currentZoom > 1:
                        self.currentZoom -= 8 # ev.angleDelta().y() / 2880
                    else:
                        return
                else:
                    self.currentZoom += 8
                mousePoint = self.viewBox.mapSceneToView(pos)

                #print("Current zoom:" + str(self.currentZoom))

                video_frame_number = int(mousePoint.x() * self.parent.currentFPS)
                #print("Zooming towards frame:" + str(video_frame_number))

                video_frame_number_visible_index = int((video_frame_number-old_left_frame)/old_total_shown_frames * self.parent.parent.currentlyShownMovieFrames)# self.parent.parent.currentlyShownMovieFrames
                need_to_substract_frames = video_frame_number_visible_index * self.currentZoom
                video_frame_number = video_frame_number - need_to_substract_frames
                if video_frame_number < 0:
                    video_frame_number = 0


                #self.parent.parent.VideoImageContainer.setPreviewCompression(None, self.parent.parent.ui.movie_slider, self.parent.parent.total_number_of_frames_generated, preview_compression_rate=self.currentZoom)
                #self.parent.parent.update_movie_strip(True)
                self.parent.parent.ui.preview_compression_slider.setValue(self.currentZoom)
                self.parent.parent.setMovieSlidePosition(self.parent.parent.ui.movie_slider_frame_number, video_frame_number)
                self.parent.parent.setMovieSliderFrameNumber(self.parent.parent.ui.movie_slider_frame_number, video_frame_number)
        elif self.parent.setControlKeyDown:
            pos = ev.position()
            if self.sceneBoundingRect().contains(pos):
                if ev.angleDelta().y() > 0:
                    self.parent.parent.ui.movie_slider.setValue(self.parent.parent.ui.movie_slider.value() - 1)
                else:
                    self.parent.parent.ui.movie_slider.setValue(self.parent.parent.ui.movie_slider.value() + 1)

    def MouseClicked(self, ev):
        if ev.button() == Qt.LeftButton:
            ev.accept()
            #print("Event!:" + str(ev.currentItem))
            #mousePoint = self.viewBox.mapSceneToView(ev.pos())
            #print("Position:" + str(mousePoint))
            #if type(ev.currentItem) == pg.PlotDataItem:
            if type(ev.currentItem) == pg.PlotCurveItem:

                mousePoint = ev.pos()
                #print("Position Line:" + str(mousePoint))
                plotContainer = self.parent.audioDataContainer.getPlots()
                has_indice = False
                for plot in plotContainer:
                    if not plotContainer[plot].isVisible:  # or not plotContainer[plot].isEditable:
                        continue
                    scatter = plotContainer[plot].getScatter()
                    pts = scatter.pointsAt(mousePoint)
                    if len(pts) != 0:
                        has_indice = True
                        #print("This is an indice")
                        break
                if not has_indice:
                    if self.singlePointIsShowing and self.parent.setShiftKeyDown and self.singlePointIndex != -1:
                        plotContainer = self.parent.audioDataContainer.getPlots()
                        plotContainer[self.parent.selectedPlot].chunk_amplitudes[self.singlePointIndex] = plotContainer[self.parent.selectedPlot].calculateChunkAmplitudeFromCurrentValue(self.singlePointValue)
                        plotContainer[self.parent.selectedPlot].chunk_modified_sample_data_amp_strength_modifiers[self.singlePointIndex] = 0
                        plotContainer[self.parent.selectedPlot].removeFromRemovedVertices([self.singlePointIndex])
                        plotContainer[self.parent.selectedPlot].setAmplitudeAndShift(shouldChangeROIminmax=True)
                        QMetaObject.invokeMethod(self.parent.parent, "showAudioWave", Qt.QueuedConnection)

                    #current_fps = self.parent.audioDataContainer.currentFPS
                    #xPos = mousePoint.x()
                    #corrected_x_pos = (xPos + 0.2 / current_fps) - ((xPos + 0.2 / current_fps) % (1 / current_fps))
                    #xShift = plotContainer[self.parent.selectedPlot].getCurrentXShift()
                    #relative_indice = int(corrected_x_pos / (1 / current_fps))
                    #relative_indice = relative_indice - xShift

                    #print("relative_indice:" + str(relative_indice))

                    #plotContainer[self.parent.selectedPlot].insertIndiceInTime(corrected_x_pos, relative_indice)

                    '''for plot in plotContainer:
                        if not plotContainer[plot].isVisible or not plotContainer[plot].isEditable:
                            continue
                        self.viewBox.change_points_colors([], plotContainer[plot])
                    plotContainer[self.parent.selectedPlot].setAmplitudeAndShift(shouldChangeROIminmax=True)
                    self.parent.showAudioWave(shouldUpdateAll=True)'''

                    #self.viewBox.change_points_colors([], plotContainer[plot], affectCopyAlso=True)
                else:
                    mousePoint = ev.pos()
                    #mousePoint = self.viewBox.mapSceneToView(pos)

                    for plot in plotContainer:
                        if not plotContainer[plot].isVisible or not plotContainer[plot].isEditable:
                            continue

                        scatter = plotContainer[plot].getScatter()
                        pts = scatter.pointsAt(mousePoint)
                        if len(pts) != 0:
                            #print("indice clicked")
                            self.dragPoint = pts[0]
                            relativeIndexSelection = self.dragPoint.index()
                            index = self.viewBox.current_scatterPlot_audioFrameLeft + relativeIndexSelection
                            xShift = plotContainer[plot].getCurrentXShift()
                            howMuchIsNotVisible = self.viewBox.current_scatterPlot_audioFrameLeft - xShift
                            if xShift < 0:
                                index = index - xShift
                            elif (self.viewBox.current_scatterPlot_audioFrameLeft - xShift) > 0:
                                index = index - xShift
                            else:
                                index = relativeIndexSelection

                            index = relativeIndexSelection  # TESTING TESTING

                            selected_indices = [index]

                            for plot2 in plotContainer:
                                if not plotContainer[plot2].isVisible or not plotContainer[plot].isEditable:
                                    continue
                                if plot != plot2:
                                    if plotContainer[plot].isVisible:
                                        plotContainer[plot].emptySelectedIndices()
                                        self.viewBox.change_points_colors([], plotContainer[plot2])

                            #self.viewBox.change_points_colors(selected_indices, plotContainer[plot], affectCopyAlso=True)
                            current_fps = self.parent.audioDataContainer.currentFPS
                            xPos = mousePoint.x()
                            corrected_x_pos = (xPos + 0.2 / current_fps) - ((xPos + 0.2 / current_fps) % (1 / current_fps))
                            #print("corrected_x_pos:" + str(corrected_x_pos))
                            #print("1 / current_fps:" + str((1 / current_fps)))
                            float_relative_indice = float(corrected_x_pos / (1 / current_fps))
                            #print("float_relative_indice:" + str(float_relative_indice))
                            relative_indice = int((plotContainer[plot].modified_sample_time_amp_strength[index] + 0.2 / current_fps) / (1 / current_fps))
                            xShift = plotContainer[self.parent.selectedPlot].getCurrentXShift()
                            #relative_indice = int(corrected_x_pos / (1 / current_fps))
                            relative_indice = relative_indice - xShift
                            #print("relative_indice:" + str(relative_indice))
                            #print("plotContainer[plot].x = " + str(plotContainer[plot].modified_sample_time_amp_strength[index]))
                            self.viewBox.change_points_colors(selected_indices, plotContainer[plot], affectCopyAlso=True, selectedIndicesOriginal=[relative_indice])
            elif type(ev.currentItem) == pg.ScatterPlotItem:
                if self.singlePointIsShowing and self.parent.setShiftKeyDown and self.singlePointIndex != -1:
                    plotContainer = self.parent.audioDataContainer.getPlots()
                    plotContainer[self.parent.selectedPlot].chunk_amplitudes[self.singlePointIndex] = plotContainer[self.parent.selectedPlot].calculateChunkAmplitudeFromCurrentValue(self.singlePointValue)
                    plotContainer[self.parent.selectedPlot].chunk_modified_sample_data_amp_strength_modifiers[self.singlePointIndex] = 0
                    plotContainer[self.parent.selectedPlot].removeFromRemovedVertices([self.singlePointIndex])
                    plotContainer[self.parent.selectedPlot].setAmplitudeAndShift(shouldChangeROIminmax=True)
                    QMetaObject.invokeMethod(self.parent.parent, "showAudioWave", Qt.QueuedConnection)

    def mouseMoved(self, evt):
        if not self.parent.audioDataContainer.shouldPlayAudio:
            if not self.viewBox.dragging:
                pos = evt
                if self.sceneBoundingRect().contains(pos):
                    mousePoint = self.viewBox.mapSceneToView(pos)
                    #print("MousePoint:" + str(mousePoint))
                    plotContainer = self.parent.audioDataContainer.getPlots()
                    for plot in plotContainer:
                        if not plotContainer[plot].isVisible: # or not plotContainer[plot].isEditable:
                            continue
                        scatter = plotContainer[plot].getScatter()
                        pts = scatter.pointsAt(mousePoint)
                        if len(pts) != 0:
                            self.dragPoint = pts[0]
                            xShift = plotContainer[plot].getCurrentXShift()
                            relativeIndexSelection = self.dragPoint.index()
                            #print("Relative Index Selection:" + str(relativeIndexSelection))
                            howMuchIsNotVisible = self.viewBox.current_scatterPlot_audioFrameLeft - xShift
                            index = relativeIndexSelection #self.viewBox.current_scatterPlot_audioFrameLeft + relativeIndexSelection
                            if xShift < 0:
                                index = index + self.viewBox.current_scatterPlot_audioFrameLeft - xShift
                            elif howMuchIsNotVisible > 0:
                                index = index + howMuchIsNotVisible
                            else:
                                index = relativeIndexSelection

                            index = relativeIndexSelection #TESTING TESTING

                            self.IndiceIsSelected[plot] = True
                            original_y_data = plotContainer[plot].getYaxis()

                            #print("Color index number:" + str(index))
                            selected_indices = [index]
                            self.viewBox.change_points_colors(selected_indices, plotContainer[plot], True)

                            coord_display_string = "Indice Value:" + str('%.2f' % float(original_y_data[index]) + " -- Time")
                            self.parent.graphWidget.setLabel('bottom', coord_display_string, units='s')
                        else: # self.IndiceIsSelected:
                            self.IndiceIsSelected[plot] = False
                            selectionOngoing = False
                            for plotSelectionDict in self.IndiceIsSelected:
                                if self.IndiceIsSelected[plotSelectionDict]:
                                    selectionOngoing = True
                                    break
                            if not selectionOngoing:
                                if self.parent.setShiftKeyDown:
                                    current_fps = self.parent.audioDataContainer.currentFPS
                                    xPos = mousePoint.x()
                                    relative_indice = round(xPos / (1 / current_fps))
                                    xShift = plotContainer[self.parent.selectedPlot].getCurrentXShift()
                                    relative_indice = relative_indice # - xShift
                                    if not plotContainer[self.parent.selectedPlot].isIndiceVisible(relative_indice- xShift):
                                        #print("show indice:" + str(relative_indice) + "   --- y:" + str(mousePoint.y()))
                                        self.viewBox.addSinglePoint(plotContainer[self.parent.selectedPlot], relative_indice, mousePoint.y(), shouldSet=False)
                                        self.singlePointIsShowing = True
                                        self.singlePointIndex = relative_indice - xShift
                                        self.singlePointValue = mousePoint.y()
                                else:
                                    self.viewBox.removeSinglePoint(plotContainer[self.parent.selectedPlot])
                                    self.singlePointIsShowing = False
                                    self.singlePointIndex = -1

                                self.viewBox.change_points_colors([], plotContainer[plot], True)
                                #self.IndiceIsSelected = False
                                coord_display_string = "Current Value:" + str('%.2f' % float(mousePoint.y()) + " -- Time")
                                self.parent.graphWidget.setLabel('bottom', coord_display_string, units='s')
            else:
                plotContainer = self.parent.audioDataContainer.getPlots()
                for plot in plotContainer:
                    if not plotContainer[plot].isVisible:  # or not plotContainer[plot].isEditable:
                        continue
                    self.viewBox.change_points_colors([], plotContainer[plot], True)

    def doLinePlot(self, x_axis = None, y_axis = None, audioFrameLeft = None, audioFrameRight = None, pen = None, audioContainer = None):
        if audioContainer == None:
            self.plot(x_axis[audioFrameLeft:audioFrameRight], y_axis[audioFrameLeft:audioFrameRight], pen=pen)
        else:
            axis_y = audioContainer.getYaxis()
            axis_x = audioContainer.getXaxis()
            if audioFrameLeft == None or audioFrameRight == None:
                audioFrameLeft = 0
                audioFrameRight = audioContainer.getAudioDataLen()
            if pen == None:
                pen = pg.mkPen(color=QColor(255, 255, 255, audioContainer.waveAlpha))
            self.plot(axis_x[audioFrameLeft:audioFrameRight], axis_y[audioFrameLeft:audioFrameRight], pen=pen)
    def getXaxis(self):
        return self.modified_sample_time
    def getYaxis(self):
        return self.modified_sample_data
    def getAudioDataLen(self):
        return len(self.modified_sample_time)
    def removeAllPlots(self):
        plotContainer = self.parent.audioDataContainer.getPlots()
        allChildren = self.viewBox.allChildren()
        for plot in plotContainer:
            for child in allChildren:
                if child == plotContainer[plot].scatter or child == plotContainer[plot].lines:
                    self.viewBox.removeItem(child)

    def doScatterPlot(self, x_axis = None, y_axis = None, audioFrameLeft = None ,audioFrameRight = None, plotName = None):
        #self.plot(x_axis[audioFrameLeft:audioFrameRight], y_axis[audioFrameLeft:audioFrameRight])
        allChildren = self.viewBox.allChildren()
        if plotName == None:
            #remove all scatter plots
            plotContainer = self.parent.audioDataContainer.getPlots()
            for plot in plotContainer:
                for child in allChildren:
                    if child == plotContainer[plot].scatter or child == plotContainer[plot].lines:
                        self.viewBox.removeItem(child)
                if not plotContainer[plot].isVisible:
                    continue

                #print("doScatterPlotFromPlot:" + str(plot))
                self.viewBox.doScatterPlotFromPlot(plotContainer[plot], audioFrameLeft, audioFrameRight)
                #self.viewBox.doScatterPlot(x_axis, y_axis, audioFrameLeft,audioFrameRight)
        else:
            audioDataContainer = self.parent.audioDataContainer
            plot = audioDataContainer.getPlot(plotName)
            if plot != None:
                for child in allChildren:
                    if child == plot.scatter or child == plot.lines:
                        self.viewBox.removeItem(child)

                if not plot.isVisible:
                    return

                self.viewBox.doScatterPlotFromPlot(plot, audioFrameLeft , audioFrameRight)
        pass


class Audio_Wave_Container():
    def __init__(self, parent, VideoImageContainer,  deforumation_settings=None, named_pipes=None, deforumation_tools=None):
        #super().__init__()
        self.parent = parent
        self.VideoImageContainer = VideoImageContainer
        self.deforumation_settings = deforumation_settings
        self.deforumationnamedpipes = named_pipes
        self.deforumation_tools = deforumation_tools
        ##Initial Checkboxvalues
        self.editable_strength_curve_checkbox = False
        self.editable_zoom_curve_checkbox = False
        self.show_strength_curve_checkbox = False
        self.show_zoom_curve_checkbox = False
        #######
        self.fps = 30
        self.showAudioFromFrame = 0
        self.shouldusethismanyFrames = 8
        self.currentFPS = 30
        self.infLines = [1,1.1,1.2,1.3]
        self.infLineArray = []
        self.cadenceLineArray = []
        self.audioPlayerLines = []
        self.currentROI = [(0,0)]
        self.currentROIarray = []
        self.currentROIarrayX = []
        self.currentROIarrayY = []
        self.currentWaveX = []
        self.currentWaveY = []
        self.copyBuffer = []
        self.copyBuffer_x = []
        self.copyBuffer_x_original = []
        self.chunk_duration_ms = 1000 / 25
        self.timeSlicePerFrame = 999
        self.currentAudioFrameWidth = 1000
        self.waveIndexPerFrame = 0
        self.currentROIminValue = 0.0
        self.currentROImaxValue = 1.0
        self.useROI = False
        self.audioDataContainer = AudioWaveDataContainer(self)
        self.audioTools = Audio_Wave_Librosa_Tools(self)
        self.current_tempo = 0
        self.current_beats = []
        #self.currentAmplitude = -1
        self.audioDataContainer.setCurrentAmplitude(-1)
        self.currentFilePath = ""
        self.currentShift = 1
        self.currentAmpShift = 0
        self.currentXShift = 0
        self.roiLine = None
        self.setShiftKeyDown = False
        self.setControlKeyDown = False
        self.setAltKeyDown = False
        self.setControlV = False
        self.shouldShowCadenceLines = False
        self.shouldOnlyBeepOnCadence = False
        #self.currentPlot = "Strength"
        #self.currentPlot2 = "Zoom"
        self.parent.ui.audio_plot_type.currentIndexChanged.connect(self.currentSelectionChanged)
        self.parent.ui.plot_color_button = pg.ColorButton(self.parent.ui.audio_synq_curve_frame)
        self.parent.ui.plot_color_button.setGeometry(QRect(104, 22, 25, 25))
        self.parent.ui.plot_color_button.setStyleSheet("QPushButton {\n    background-color: rgb(108,108,118); /* Matching the tab's base color */\n    border: none;\n    border-radius: 0px; /* Consistent with the tab's rounded corners */\n    padding: 0px 0px; /* Comfortable padding for the button text */\n    color: white; /* White text for contrast */\n    text-align: center;\n\n}\n\nQPushButton:hover {\n    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n\n}\n\nQPushButton:pressed {\n    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n\n}")
        self.parent.ui.plot_color_button.sigColorChanging.connect(self.changePlotColor)


        #self.strengthPlotName = "Strength"
        #self.zoomPlotName = "Zoom"
        self.availablePlots = ["Strength","Zoom","PanLR","PanUD", "RotateH", "RotateV", "Tilt"]
        self.selectedPlot = self.availablePlots[0]

        self.shouldUseMetronomeUnderValue = False
        self.shouldUseMetronomeOverValue = False
        self.metronomeUnderValue = 0.2
        self.metronomeOverValue = 1.0

        #print("Using plot name:" + str(self.currentPlot))
        '''self.setWindowTitle("Waveform Viewer")

        # Setting up the central widget and layout
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        layout = QVBoxLayout(self.centralWidget)'''

        # Graph widget
        self.graphWidget = CustomPlotWidget(self) #pg.PlotWidget()
        #self.graphWidget.mousePressEvent()
        #self.graphWidget.installEventFilter(parent)
        #pg.PlotWidget.obje
        #self.graphWidget.ob

        #self.graphWidget.
        self.parent.ui.gridLayout_audio_screen.addWidget(self.graphWidget)

        # Button to open wave file
        #self.openFileButton = QPushButton("Open Wave File")

        #self.parent.ui.gridLayout_audio_screen.addWidget(self.openFileButton)
        #self.openFileButton.clicked.connect(self.openFileDialog)

        self.graphWidget.viewBox.setAudioRange(0,28)
        self.graphWidget.setMouseEnabled(x=True, y=False)
        #y = [0, 100]
        #x = [1, 1]
        #self.graphWidget.plot(x, y, pen=pg.mkPen('b', width=5))
        #self.graphWidget.InfiniteLine(pos=1, angle=90, movable=False)
        '''for x in self.infLines:
            self.infLineArray.append(pg.InfiniteLine(pos=x, angle=90, pen=pg.mkPen(color=QColor(255, 0, 0, 40), width=2), span=(0, 0.5), movable=False))
        for infLine in self.infLineArray:
            self.graphWidget.addItem(infLine)'''
        #self.graphWidget.removeItem(self.vLine)

    def changePlotColor(self, something):
        color = something.color()
        print("Should change plot color:" + str(color))
        color2 = QColor(255, 255, 0, 180)
        print("Should change plot color:" + str(color2))
        plotContainer = self.audioDataContainer.getPlots()
        if self.selectedPlot in plotContainer:
            plotContainer[self.selectedPlot].setPlotColor(color)
            if plotContainer[self.selectedPlot].isVisible:
                self.graphWidget.viewBox.change_points_colors([], plotContainer[self.selectedPlot])
            color_array = color.rgb()
            self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.selectedPlot+"_color", color_array)


    def updateAudioPlayerLine(self):
        for audioPlayerLine in self.audioPlayerLines:
            self.graphWidget.removeItem(audioPlayerLine)
        self.audioPlayerLines = []
        audioPlayStartPosition = self.audioDataContainer.currentAudioPlayerStartPositionXaxis
        self.audioPlayerLines.append(pg.InfiniteLine(pos=audioPlayStartPosition, angle=90, pen=pg.mkPen(color=QColor(255, 255, 0, 180), width=4), span=(0, 1.0), movable=False))
        self.audioPlayerStartLine = [0]
        for audioPlayerLine in self.audioPlayerLines:
            self.graphWidget.addItem(audioPlayerLine)
        currentImageShowing = int(self.currentFPS * audioPlayStartPosition) # float(self.showAudioFromFrame * videoCompressionRate / self.currentFPS)
        #print("AudioPlayerNeedle over frame:" + str(currentImageShowing))
        videoCompressionRate = self.VideoImageContainer.getPreviewCompression()
        currently_shown_left_frame = self.parent.ui.movie_slider.value() * videoCompressionRate
        currently_shown_right_frame = currently_shown_left_frame + self.parent.currentlyShownMovieFrames * videoCompressionRate
        #print("Showing frames:" + str(currently_shown_left_frame) + " - " + str(currently_shown_right_frame))
        if (currentImageShowing > currently_shown_right_frame) or (currentImageShowing < currently_shown_left_frame):
            #self.parent.ui.movie_slider_frame_number.
            #self.parent.ui.movie_slider.setValue()
            self.parent.setMovieSlidePosition(self.parent.ui.movie_slider_frame_number, currentImageShowing)
            self.parent.setMovieSliderFrameNumber(self.parent.ui.movie_slider_frame_number, currentImageShowing)

    def showAudioWave(self, showAudioFromFrame = None, shouldusethismanyFrames = None, currentFPS = None, shouldUpdateAll = False):
        waveIndexPerFrame = self.audioDataContainer.getwaveIndexPerFrame()
        if waveIndexPerFrame != 0:
            timeLeft = 0
            timeRight = 0
            if showAudioFromFrame == None:
                self.currentFPS = float(self.parent.ui.replay_fps_input_box.text())
                shouldusethismanyFrames = self.parent.currentlyShownMovieFrames #self.shouldusethismanyFrames
                self.shouldusethismanyFrames = shouldusethismanyFrames
            else:
                self.showAudioFromFrame = showAudioFromFrame
                self.shouldusethismanyFrames = shouldusethismanyFrames
                self.currentFPS = currentFPS
            if self.currentFPS <= 0:
                self.currentFPS = 1
            if self.currentFPS != self.audioDataContainer.getCurrentFPS() or shouldUpdateAll:
                self.audioDataContainer.setCurrentFPS(self.currentFPS)
                waveIndexPerFrame = self.audioDataContainer.getwaveIndexPerFrame()
                self.audioDataContainer.revertToOriginal()
                self.audioDataContainer.setAmplitudeRangeZeroOne()#plotName=self.strengthPlotName)
                self.audioDataContainer.downSampleExisting(100000)
                #currentPlot = self.audioDataContainer.getPlot(self.strengthPlotName)
                #currentPlot.setAmplitudeAndShift()


            videoCompressionRate = self.VideoImageContainer.getPreviewCompression()
            timeLeft = float(self.showAudioFromFrame*videoCompressionRate / self.currentFPS)
            timeRight = float(self.showAudioFromFrame*videoCompressionRate / self.currentFPS + self.shouldusethismanyFrames*videoCompressionRate/self.currentFPS)
            frameLeftROI = self.showAudioFromFrame*videoCompressionRate
            frameRightROI = frameLeftROI + self.shouldusethismanyFrames*videoCompressionRate
            safeFrameForAudioDisplay = 1 #show one extra audio frame chunk left and right of visible area
            if self.showAudioFromFrame > 0:
                audioFrameLeft = int(((self.showAudioFromFrame-safeFrameForAudioDisplay)*videoCompressionRate) * waveIndexPerFrame)
            else:
                audioFrameLeft = 0
            audioFrameRight = int(((self.showAudioFromFrame*videoCompressionRate) * waveIndexPerFrame) + (((self.shouldusethismanyFrames + safeFrameForAudioDisplay)*videoCompressionRate) * waveIndexPerFrame))

            totalTime = timeRight - timeLeft
            audframeWidth = self.parent.ui.audio_clip.width()
            self.currentAudioFrameWidth = audframeWidth
            #print("audframeWidth:" + str(audframeWidth))
            xInfLineEvery = float(totalTime/shouldusethismanyFrames)
            #print("shouldusethismanyFrames:" + str(shouldusethismanyFrames))
            frameSizeInTime = float(totalTime/(frameRightROI-frameLeftROI))
            #print("frameRightROI-frameLeftROI:" + str(frameRightROI-frameLeftROI))
            #print("frameLeft:" + str(frameLeftROI))
            #print("frameRight:" + str(frameRightROI))
            self.timeSlicePerFrame = xInfLineEvery
            #print("xInfLineEvery:" + str(xInfLineEvery))

            #Clear and redraw wave
            self.graphWidget.clear()
            #Set viewbox
            self.graphWidget.viewBox.setAudioRange(timeLeft, timeRight)

            #Paint the audio wave
            self.graphWidget.doLinePlot(audioContainer=self.audioDataContainer, audioFrameLeft=audioFrameLeft, audioFrameRight=audioFrameRight, pen=pg.mkPen(color=QColor(255, 255, 255, self.audioDataContainer.waveAlpha)))

            #Paint the frame start helper lines
            for infLine in self.infLineArray:
                self.graphWidget.removeItem(infLine)
            self.infLineArray = []
            for x in range(0, shouldusethismanyFrames):
                self.infLineArray.append(pg.InfiniteLine(pos=timeLeft + (xInfLineEvery * x), angle=90, pen=pg.mkPen(color=QColor(255, 0, 0, 40), width=2), span=(0, 0.5), movable=False))
                #print("Line on time axis:" + str(timeLeft + (xInfLineEvery * x)))
            for infLine in self.infLineArray:
                self.graphWidget.addItem(infLine)

            #Paint the Audio player needle
            for audioPlayerLine in self.audioPlayerLines:
                self.graphWidget.removeItem(audioPlayerLine)
            self.audioPlayerLines = []
            audioPlayStartPosition = self.audioDataContainer.currentAudioPlayerStartPositionXaxis
            self.audioPlayerLines.append(pg.InfiniteLine(pos=audioPlayStartPosition, angle=90, pen=pg.mkPen(color=QColor(255, 255, 0, 180), width=4), span=(0, 1.0), movable=False))
            self.audioPlayerStartLine = [0]
            for audioPlayerLine in self.audioPlayerLines:
                self.graphWidget.addItem(audioPlayerLine)

            #Paint the graphs
            self.graphWidget.doScatterPlot(audioFrameLeft=frameLeftROI, audioFrameRight=frameRightROI+1)

            minVal = self.audioDataContainer.getcurrentPlotMinValue()
            maxVal = self.audioDataContainer.getcurrentPlotMaxValue()
            self.graphWidget.setYRange(minVal, maxVal)

            #Paint the bottom of plot line
            self.vLine = pg.InfiniteLine(pos=minVal, angle=0, pen=pg.mkPen('g', width=1), movable=False)
            self.graphWidget.addItem(self.vLine)

            #Paint the metronome threshold lines
            if self.shouldUseMetronomeOverValue:
                self.vOverValueLine = pg.InfiniteLine(pos=self.metronomeOverValue, angle=0, pen=pg.mkPen('b', width=1), movable=False)
                self.graphWidget.addItem(self.vOverValueLine)

            if self.shouldUseMetronomeUnderValue:
                self.vUnderValueLine = pg.InfiniteLine(pos=self.metronomeUnderValue, angle=0, pen=pg.mkPen('r', width=1), movable=False)
                self.graphWidget.addItem(self.vUnderValueLine)

            #Paint the cadence helper lines
            if self.shouldShowCadenceLines:
                for infLine in self.cadenceLineArray:
                    self.graphWidget.removeItem(infLine)
                self.cadenceLineArray = []
                currentCadence = self.parent.DeforumationMotions.cadence
                for x in range(frameLeftROI, frameRightROI):
                    if x % currentCadence == 0:
                        self.cadenceLineArray.append(pg.InfiniteLine(pos=(frameSizeInTime * x), angle=90, pen=pg.mkPen(color=QColor(255, 255, 255, 255), width=2), span=(0, 1), movable=False))
                    #print("Line on time axis:" + str(timeLeft + (xInfLineEvery * x)))
                for infLine in self.cadenceLineArray:
                    self.graphWidget.addItem(infLine)

            # Set Viewbox labels
            self.graphWidget.setLabel('left', 'Value')  # , units='d')


    def openFileDialog(self):
        filePath, _ = QFileDialog.getOpenFileName(self.parent, "Open Wave File", "", "Wave Files (*.wav)")
        if filePath:
            self.loadAndPlotWave(filePath)

    # simple peak detection
    def peak_detect(self, data):
        max_val = np.amax(abs(data))
        peak_ndx = np.where(data >= 0)
        if len(peak_ndx[0]) == 0:  # if nothing found then the max must be negative
            peak_ndx = np.where(data == -max_val)
        return peak_ndx

    def loadAndPlotWave(self, filePath):
        # Read wave file
        self.audioDataContainer.shouldPlayAudio = False
        self.audioDataContainer.shouldCloseAudioPlayer = True
        self.graphWidget.clear()
        #self.audioData.readWaveFile(filePath) # original_sample_rate, self.audioData.original_sample_data = wavfile.read(filePath)
        self.currentFilePath = filePath
        ret = self.audioDataContainer.readWaveFile(filePath, downsample=100000)
        if ret == -1:
            return -1

        self.current_tempo, self.current_beats = self.audioTools.getAudioBPM(filePath)
        #print("This audio file has BPM:" + str(beats))
        audio_misc_info_bpm_label = ""
        audio_misc_info_bpm_label += "Predicted audio file has BPM:" + str(self.current_tempo) + "\n"

        current_tempo = math.floor(self.current_tempo)
        audio_misc_info_bpm_label += "Calculations done on BPM::" + str(current_tempo)
        for n in range(5, current_tempo + 1):
            fps_is_ok = current_tempo % n
            cadence = ""
            if fps_is_ok == 0:
                frames_per_beat = round((60 / current_tempo) / (1 / n))
                first_c = True
                for c in range(1, frames_per_beat+1):
                    if (frames_per_beat % c) == 0:
                        if first_c:
                            cadence += str(c)
                            first_c = False
                        else:
                            cadence += ", " + str(c)
                audio_misc_info_bpm_label += "\nUsing " + str(n) + " FPS, will land a beat every " + str(frames_per_beat) + " frames, (use cadence: " + cadence + ")"

        current_tempo = math.ceil(self.current_tempo)
        audio_misc_info_bpm_label += "\n\nCalculations done on BPM::" + str(current_tempo)
        for n in range(5,current_tempo+1):
            fps_is_ok = current_tempo % n
            cadence = ""
            if fps_is_ok == 0:
                frames_per_beat = round((60/current_tempo) / (1/n))
                first_c = True
                for c in range(1,frames_per_beat+1):
                    if (frames_per_beat % c) == 0:
                        if first_c:
                            cadence += str(c)
                            first_c = False
                        else:
                            cadence += ", " + str(c)
                audio_misc_info_bpm_label += "\nUsing " + str(n) + " FPS, will land a beat every " + str(frames_per_beat) + " frames, (use cadence: " + cadence + ")"


        self.parent.ui.audio_misc_info_bpm_edit.setText(audio_misc_info_bpm_label)
        fps = self.currentFPS = int(self.parent.ui.replay_fps_input_box.text())
        #self.audioData.setCurrentFPS(fps)
        self.audioDataContainer.setCurrentFPS(fps)
        plotContainer = self.audioDataContainer.getPlots()
        if len(plotContainer) != 0:
            print("Already plots in plotcontainer... deleting")
            self.graphWidget.removeAllPlots()
            self.audioDataContainer.plotDataContainer.clear() # = {}
        #Create a plot in the audio data container
        for plot in self.availablePlots:
            self.audioDataContainer.addPlot(plot, pen=None, brush=None)#pg.mkBrush(color=(255, 0, 0, 255))) #pg.mkPen(color=(255, 0, 0, 255), width=2), brush=pg.mkBrush(color=(255, 0, 0, 255)))

        self.setComponetValues()

        #self.audioDataContainer.addPlot(self.strengthPlotName, pen=pg.mkPen(color=(255, 0, 0, 255), width=2), brush=pg.mkBrush(color=(255, 0, 0, 255)))
        #self.audioDataContainer.addPlot(self.zoomPlotName, pen=pg.mkPen(color=(0, 0, 255, 255), width=2), brush=pg.mkBrush(color=(0, 0, 255, 255)))

        self.audioDataContainer.setAmplitudeRangeZeroOne(plotName=self.selectedPlot)
        #self.audioDataContainer.setAmplitudeRangeZeroOne(plotName=self.currentPlot2)


        for plot in self.availablePlots:
            self.graphWidget.doScatterPlot(plotName=plot)
            plotContainer[plot].chunk_scatter_brushes = [plotContainer[plot].original_indice_middle for _ in range(len(plotContainer[plot].chunk_amplitudes))]
            plotContainer[plot].chunk_scatter_pens = [plotContainer[plot].original_indice_outer for _ in range(len(plotContainer[plot].chunk_amplitudes))]

            #self.graphWidget.doScatterPlot(plotName=plot)
        #self.audioDataContainer.setYAxisRange(self.zoomPlotName, 8)
        #-----------------------------------------------------------------------------------------------------------------------

        #self.audioData.setAmplitudeRangeZeroOne(self.ROIData.currentROIminValue, self.ROIData.currentROImaxValue)
        #self.audioData.downSample(100000)

        self.graphWidget.setLabel('bottom', 'Time', units='s')
        self.graphWidget.setLabel('left', 'Strength')
        #self.graphWidget.doLinePlot(self.audioData.modified_sample_time, self.audioData.modified_sample_data, 0, len(self.audioData.modified_sample_time), pg.mkPen(color=QColor(255, 255, 255, self.audioData.waveAlpha)))
        self.graphWidget.doLinePlot(audioContainer=self.audioDataContainer, pen=pg.mkPen(color=QColor(255, 255, 255, self.audioDataContainer.waveAlpha)))
        self.showAudioWave(shouldUpdateAll=True)
        #self.graphWidget.show()

        return 0
    def savePlotsAndAudioSettingsToFile(self, file_name):
        plotContainer = self.audioDataContainer.getPlots()
        self.p = {}
        self.p["FPS"] = self.audioDataContainer.getCurrentFPS()
        self.p["FilePath"] = self.currentFilePath
        for plot in plotContainer:
            self.p[plot + "_orginal_modified_sample_time_amp_strength"] = plotContainer[plot].orginal_modified_sample_time_amp_strength.tolist()
            self.p[plot + "_chunk_amplitudes"] = plotContainer[plot].chunk_amplitudes
            self.p[plot + "_chunk_modified_sample_data_amp_strength_modifiers"] = plotContainer[plot].chunk_modified_sample_data_amp_strength_modifiers.tolist()
            self.p[plot + "_modified_sample_data_amp_strength_modifiers_removed_vertices"] = plotContainer[plot].modified_sample_data_amp_strength_modifiers_removed_vertices
            self.p[plot + "_amplitude"] = plotContainer[plot].currentAmplitude
            self.p[plot + "_shift"] = plotContainer[plot].currentShift
            self.p[plot + "_ampshift"] = plotContainer[plot].currentAmpShift
            self.p[plot + "_xshift"] = plotContainer[plot].currentXShift

        with open(file_name, "w") as jsonfile:
            try:
                json.dump(self.p, jsonfile)
            except Exception as e:
                print("Error saving audio settings file:" + str(e))
                return -1

    def loadPlotsAndAudioSettingsFromFile(self, file_name):

        with open(file_name, "r", encoding='utf-8') as jsonfile:
            try:
                self.p = json.load(jsonfile)
            except Exception as e:
                print("Error loading audio settings file:" + str(e))
                return -1

        if "FilePath" in self.p:
            ret = self.loadAndPlotWave(self.p["FilePath"])
            if ret == -1:
                return -1

        if "FPS" in self.p:
            fps = int(self.p["FPS"])
            self.audioDataContainer.setCurrentFPS(fps)
            sender = self.parent.ui.replay_fps_input_box
            sender.setText(str(fps))
            self.parent.VideoImageContainer.saveFPStoConfig(sender)


        plotContainer = self.audioDataContainer.getPlots()
        for plot in plotContainer:
            if plot + "_orginal_modified_sample_time_amp_strength" in self.p:
                plotContainer[plot].orginal_modified_sample_time_amp_strength = np.array(self.p[plot + "_orginal_modified_sample_time_amp_strength"])
                plotContainer[plot].chunk_amplitudes = self.p[plot + "_chunk_amplitudes"]
                plotContainer[plot].chunk_modified_sample_data_amp_strength_modifiers = np.array(self.p[plot + "_chunk_modified_sample_data_amp_strength_modifiers"])
                plotContainer[plot].modified_sample_data_amp_strength_modifiers_removed_vertices = self.p[plot + "_modified_sample_data_amp_strength_modifiers_removed_vertices"]
                plotContainer[plot].modified_sample_data_amp_strength_modifiers_removed_vertices = unique(plotContainer[plot].modified_sample_data_amp_strength_modifiers_removed_vertices)

                if plot + "_amplitude" in self.p:
                    plotContainer[plot].currentAmplitude = self.p[plot + "_amplitude"]
                if plot + "_shift" in self.p:
                    plotContainer[plot].currentShift = self.p[plot + "_shift"]
                if plot + "_ampshift" in self.p:
                    plotContainer[plot].currentAmpShift = self.p[plot + "_ampshift"]
                if plot + "_xshift" in self.p:
                    plotContainer[plot].currentXShift = self.p[plot + "_xshift"]

                plotContainer[plot].chunk_scatter_brushes = [plotContainer[plot].original_indice_middle for _ in range(len(plotContainer[plot].chunk_amplitudes))]
                plotContainer[plot].chunk_scatter_pens = [plotContainer[plot].original_indice_outer for _ in range(len(plotContainer[plot].chunk_amplitudes))]

                plotContainer[plot].setAmplitudeAndShift(shouldChangeROIminmax=True)
                self.showAudioWave(shouldUpdateAll=True)

        if self.selectedPlot in plotContainer:
            self.parent.ui.amplitude_value_box.setText(str(plotContainer[self.selectedPlot].currentAmplitude))
            self.parent.ui.ampshift_value_box.setText(str(plotContainer[self.selectedPlot].currentAmpShift))
            self.parent.ui.shift_value_box.setText(str(plotContainer[self.selectedPlot].currentShift))
            self.parent.ui.shift_leftright_value_box.setText(str(plotContainer[self.selectedPlot].currentXShift))

    def convertMP3toWav(self,mp3_file_name, wav_file_name):
        # convert wav to mp3
        sound = AudioSegment.from_mp3(mp3_file_name)
        sound.export(wav_file_name, format="wav")

    def clicked_button(self, sender, event = None):
        #currentPlot = self.audioDataContainer.getPlot(self.currentPlot)

        plotContainer = self.audioDataContainer.getPlots()
        if sender.objectName().startswith("Save_Audio_Settings"):
            file_name, _ = QFileDialog.getSaveFileName(self.parent, "Save current audio wave settings", "", "Config File(*.json)")
            if file_name != "" and file_name != None:
                self.savePlotsAndAudioSettingsToFile(file_name)
                return
        elif sender.objectName().startswith("Load_Audio_Settings"):
            file_name, _ = QFileDialog.getOpenFileName(self.parent, "Load audio wave settings", "", "All (*.json)")
            if file_name != "" and file_name != None:
                self.loadPlotsAndAudioSettingsFromFile(file_name)
                return
        elif sender.objectName().startswith("Convert_MP3_to_Wave"):
            mp3_file_name, _ = QFileDialog.getOpenFileName(self.parent, "Choose mp3 file to convert", "", "MP3 File (*.mp3)")
            if mp3_file_name != "" and mp3_file_name != None:
                wav_file_name, _ = QFileDialog.getSaveFileName(self.parent, "Save converted mp3 file to", "", "Wave File(*.wav)")
                if wav_file_name != "" and wav_file_name != None:
                    self.convertMP3toWav(mp3_file_name, wav_file_name)
                    return
        elif self.selectedPlot in plotContainer:
            currentPlot = plotContainer[self.selectedPlot]
            #getEditableCurve =
            if sender.objectName().startswith("amplitude_increase_button"):
                self.currentAmplitude = round(float(self.parent.ui.amplitude_value_box.text())+0.01,2)
                self.parent.ui.amplitude_value_box.setText(str(self.currentAmplitude))
                self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.selectedPlot + "_amplitude", self.currentAmplitude) #Write to GuiConfig
                currentPlot.setAmplitudeAndShift(amplitude=self.currentAmplitude, shouldChangeROIminmax=True)
                self.audioDataContainer.revertToOriginal()
                self.audioDataContainer.setCurrentFPS(self.currentFPS)
                self.audioDataContainer.setAmplitudeRangeZeroOne(plotName=self.selectedPlot)#self.currentPlot)
                self.audioDataContainer.downSampleExisting(100000)
                self.showAudioWave(shouldUpdateAll=True)
                if currentPlot.should_synq_with_mediator:
                    self.sendGraphToMediator(self.selectedPlot, True)
            elif sender.objectName().startswith("amplitude_decrease_button"):
                self.currentAmplitude = round(float(self.parent.ui.amplitude_value_box.text()) - 0.01, 2)
                self.parent.ui.amplitude_value_box.setText(str(self.currentAmplitude))
                self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.selectedPlot + "_amplitude", self.currentAmplitude) #Write to GuiConfig
                currentPlot.setAmplitudeAndShift(amplitude=self.currentAmplitude, shouldChangeROIminmax=True)
                self.audioDataContainer.revertToOriginal()
                self.audioDataContainer.setCurrentFPS(self.currentFPS)
                self.audioDataContainer.setAmplitudeRangeZeroOne(plotName=self.selectedPlot)#=self.currentPlot)
                self.audioDataContainer.downSampleExisting(100000)
                self.showAudioWave(shouldUpdateAll=True)
                if currentPlot.should_synq_with_mediator:
                    self.sendGraphToMediator(self.selectedPlot, True)
            if sender.objectName().startswith("ampshift_increase_button"):
                self.currentAmpShift = round(float(self.parent.ui.ampshift_value_box.text())+0.01,2)
                self.parent.ui.ampshift_value_box.setText(str(self.currentAmpShift))
                self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.selectedPlot + "_ampshift", self.currentAmpShift) #Write to GuiConfig
                currentPlot.setAmplitudeAndShift(ampshift=self.currentAmpShift, shouldChangeROIminmax=True)
                self.audioDataContainer.revertToOriginal()
                self.audioDataContainer.setCurrentFPS(self.currentFPS)
                self.audioDataContainer.setAmplitudeRangeZeroOne(plotName=self.selectedPlot)#self.currentPlot)
                self.audioDataContainer.downSampleExisting(100000)
                self.showAudioWave(shouldUpdateAll=True)
                if currentPlot.should_synq_with_mediator:
                    self.sendGraphToMediator(self.selectedPlot, True)
            elif sender.objectName().startswith("ampshift_decrease_button"):
                self.currentAmpShift = round(float(self.parent.ui.ampshift_value_box.text()) - 0.01, 2)
                self.parent.ui.ampshift_value_box.setText(str(self.currentAmpShift))
                self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.selectedPlot + "_ampshift", self.currentAmpShift) #Write to GuiConfig
                currentPlot.setAmplitudeAndShift(ampshift=self.currentAmpShift, shouldChangeROIminmax=True)
                self.audioDataContainer.revertToOriginal()
                self.audioDataContainer.setCurrentFPS(self.currentFPS)
                self.audioDataContainer.setAmplitudeRangeZeroOne(plotName=self.selectedPlot)#=self.currentPlot)
                self.audioDataContainer.downSampleExisting(100000)
                self.showAudioWave(shouldUpdateAll=True)
                if currentPlot.should_synq_with_mediator:
                    self.sendGraphToMediator(self.selectedPlot, True)
            elif sender.objectName().startswith("shift_increase_button"):
                self.currentShift = round(float(self.parent.ui.shift_value_box.text())+0.01,2)
                self.parent.ui.shift_value_box.setText(str(self.currentShift))
                self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.selectedPlot + "_shift", self.currentShift) #Write to GuiConfig
                currentPlot.setAmplitudeAndShift(shift=self.currentShift, shouldChangeROIminmax=True)
                self.audioDataContainer.revertToOriginal()
                self.audioDataContainer.setCurrentFPS(self.currentFPS)
                self.audioDataContainer.setAmplitudeRangeZeroOne(plotName=self.selectedPlot)#=self.currentPlot)
                self.audioDataContainer.downSampleExisting(100000)
                self.showAudioWave(shouldUpdateAll=True)
                if currentPlot.should_synq_with_mediator:
                    self.sendGraphToMediator(self.selectedPlot, True)
            elif sender.objectName().startswith("shift_decrease_button"):
                self.currentShift = round(float(self.parent.ui.shift_value_box.text()) - 0.01, 2)
                self.parent.ui.shift_value_box.setText(str(self.currentShift))
                self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.selectedPlot + "_shift", self.currentShift) #Write to GuiConfig
                currentPlot.setAmplitudeAndShift(shift=self.currentShift, shouldChangeROIminmax=True)
                self.audioDataContainer.revertToOriginal()
                self.audioDataContainer.setCurrentFPS(self.currentFPS)
                self.audioDataContainer.setAmplitudeRangeZeroOne(plotName=self.selectedPlot)#=self.currentPlot)
                self.audioDataContainer.downSampleExisting(100000)
                self.showAudioWave(shouldUpdateAll=True)
                if currentPlot.should_synq_with_mediator:
                    self.sendGraphToMediator(self.selectedPlot, True)
            elif sender.objectName().startswith("amplitude_value_box"):
                self.currentAmplitude = round(float(self.parent.ui.amplitude_value_box.text()), 2)
                self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.selectedPlot + "_amplitude", self.currentAmplitude) #Write to GuiConfig
                currentPlot.setAmplitudeAndShift(amplitude=self.currentAmplitude, shouldChangeROIminmax=True)
                self.audioDataContainer.revertToOriginal()
                self.audioDataContainer.setCurrentFPS(self.currentFPS)
                self.audioDataContainer.setAmplitudeRangeZeroOne(plotName=self.selectedPlot)#=self.currentPlot)
                self.audioDataContainer.downSampleExisting(100000)
                self.showAudioWave(shouldUpdateAll=True)
                if currentPlot.should_synq_with_mediator:
                    self.sendGraphToMediator(self.selectedPlot, True)
            elif sender.objectName().startswith("shift_value_box"):
                self.currentShift = round(float(self.parent.ui.shift_value_box.text()), 2)
                self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.selectedPlot + "_shift", self.currentShift) #Write to GuiConfig
                currentPlot.setAmplitudeAndShift(shift=self.currentShift, shouldChangeROIminmax=True)
                self.audioDataContainer.revertToOriginal()
                self.audioDataContainer.setCurrentFPS(self.currentFPS)
                self.audioDataContainer.setAmplitudeRangeZeroOne(plotName=self.selectedPlot)#=self.currentPlot)
                self.audioDataContainer.downSampleExisting(100000)
                self.showAudioWave(shouldUpdateAll=True)
                if currentPlot.should_synq_with_mediator:
                    self.sendGraphToMediator(self.selectedPlot, True)
            elif sender.objectName().startswith("ampshift_value_box"):
                self.currentAmpShift = round(float(self.parent.ui.ampshift_value_box.text()), 2)
                self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.selectedPlot + "_ampshift", self.currentAmpShift) #Write to GuiConfig
                currentPlot.setAmplitudeAndShift(ampshift=self.currentAmpShift, shouldChangeROIminmax=True)
                self.audioDataContainer.revertToOriginal()
                self.audioDataContainer.setCurrentFPS(self.currentFPS)
                self.audioDataContainer.setAmplitudeRangeZeroOne(plotName=self.selectedPlot)#=self.currentPlot)
                self.audioDataContainer.downSampleExisting(100000)
                self.showAudioWave(shouldUpdateAll=True)
                if currentPlot.should_synq_with_mediator:
                    self.sendGraphToMediator(self.selectedPlot, True)
            elif sender.objectName().startswith("shift_leftright_value_box"):
                self.currentXShift = int(self.parent.ui.shift_leftright_value_box.text())
                self.parent.ui.shift_leftright_value_box.setText(str(self.currentXShift))
                self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.selectedPlot + "_shiftleftright", self.currentXShift) #Write to GuiConfig
                currentPlot.setAmplitudeAndShift(xshift=self.currentXShift, shouldChangeROIminmax=True)
                self.showAudioWave(shouldUpdateAll=True)
                if currentPlot.should_synq_with_mediator:
                    self.sendGraphToMediator(self.selectedPlot, True)
            elif sender.objectName().startswith("shift_left_button"):
                self.currentXShift = int(self.parent.ui.shift_leftright_value_box.text())-1
                self.parent.ui.shift_leftright_value_box.setText(str(self.currentXShift))
                self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.selectedPlot + "_shiftleftright", self.currentXShift) #Write to GuiConfig
                currentPlot.setAmplitudeAndShift(xshift=self.currentXShift, shouldChangeROIminmax=True)
                self.showAudioWave(shouldUpdateAll=True)
                if currentPlot.should_synq_with_mediator:
                    self.sendGraphToMediator(self.selectedPlot, True)
            elif sender.objectName().startswith("shift_right_button"):
                self.currentXShift = int(self.parent.ui.shift_leftright_value_box.text())+1
                self.parent.ui.shift_leftright_value_box.setText(str(self.currentXShift))
                self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.selectedPlot + "_shiftleftright", self.currentXShift) #Write to GuiConfig
                currentPlot.setAmplitudeAndShift(xshift=self.currentXShift, shouldChangeROIminmax=True)
                self.showAudioWave(shouldUpdateAll=True)
                if currentPlot.should_synq_with_mediator:
                    self.sendGraphToMediator(self.selectedPlot, True)


            for plot in plotContainer:
                if not plotContainer[plot].isEditable or not plotContainer[plot].isVisible:
                    continue
                currentPlot = plotContainer[plot]
                if sender.objectName().startswith("change_audio_value_increase_button"):
                    if plotContainer[plot].hasSelectedIndices():
                        currentPlot.addValueToIndices(0.1)
                        currentPlot.setAmplitudeAndShift(shouldChangeROIminmax=True)
                        self.showAudioWave(shouldUpdateAll=True)
                        if currentPlot.should_synq_with_mediator:
                            self.sendGraphToMediator(plot, True)
                elif sender.objectName().startswith("change_audio_value_decrease_button"):
                    if plotContainer[plot].hasSelectedIndices():
                        currentPlot.addValueToIndices(-0.1)
                        currentPlot.setAmplitudeAndShift(shouldChangeROIminmax=True)
                        self.showAudioWave(shouldUpdateAll=True)
                        if currentPlot.should_synq_with_mediator:
                            self.sendGraphToMediator(plot, True)
                elif sender.objectName().startswith("change_audio_value_high_button"):
                    if plotContainer[plot].hasSelectedIndices():
                        currentPlot.setIndiceValueHighAmp(None)
                        currentPlot.setAmplitudeAndShift(shouldChangeROIminmax=True)
                        self.showAudioWave(shouldUpdateAll=True)
                        if currentPlot.should_synq_with_mediator:
                            self.sendGraphToMediator(plot, True)
                elif sender.objectName().startswith("change_audio_value_middle_button"):
                    if plotContainer[plot].hasSelectedIndices():
                        currentPlot.setIndiceValueMiddleAmp(None)
                        currentPlot.setAmplitudeAndShift(shouldChangeROIminmax=True)
                        self.showAudioWave(shouldUpdateAll=True)
                        if currentPlot.should_synq_with_mediator:
                            self.sendGraphToMediator(plot, True)
                elif sender.objectName().startswith("change_audio_value_low_button"):
                    if plotContainer[plot].hasSelectedIndices():
                        currentPlot.setIndiceValueLowAmp(None)
                        currentPlot.setAmplitudeAndShift(shouldChangeROIminmax=True)
                        self.showAudioWave(shouldUpdateAll=True)
                        if currentPlot.should_synq_with_mediator:
                            self.sendGraphToMediator(plot, True)
                elif sender.objectName().startswith("change_audio_value_zero_button"):
                    if plotContainer[plot].hasSelectedIndices():
                        currentPlot.setIndiceValue(None, 0)
                        currentPlot.setAmplitudeAndShift(shouldChangeROIminmax=True)
                        self.showAudioWave(shouldUpdateAll=True)
                        if currentPlot.should_synq_with_mediator:
                            self.sendGraphToMediator(plot, True)
                elif sender.objectName().startswith("change_audio_value_org_button"):
                    if plotContainer[plot].hasSelectedIndices():
                        currentPlot.setIndiceValueOrgAmp(None)
                        currentPlot.setAmplitudeAndShift(shouldChangeROIminmax=True)
                        self.showAudioWave(shouldUpdateAll=True)
                        if currentPlot.should_synq_with_mediator:
                            self.sendGraphToMediator(plot, True)
                elif sender.objectName().startswith("cadence_change_audio_value_button"):
                    if plot == self.selectedPlot and  plotContainer[plot].hasSelectedIndices():
                        cadence_change_audio_value = round(float(self.parent.ui.cadence_change_audio_value_box.text()), 3)
                        cadence_change_audio_gap_value = round(float(self.parent.ui.cadence_change_audio_value_gap_box.text()), 3)
                        cadence_change_audio_other_value = round(float(self.parent.ui.cadence_change_audio_value_others_box.text()), 3)
                        currentPlot.setIndiceValueOnCadenceSteps(cadence_change_audio_value, cadence_change_audio_gap_value, cadence_change_audio_other_value)
                        currentPlot.setAmplitudeAndShift(shouldChangeROIminmax=True)
                        self.showAudioWave(shouldUpdateAll=True)
                        if currentPlot.should_synq_with_mediator:
                            self.sendGraphToMediator(plot, True)


        if sender.objectName().startswith("change_audio_value_button"):
            plotContainer = self.audioDataContainer.getPlots()
            isThereAnySelection = self.audioDataContainer.isThereAnySelection()
            fromValue = round(float(self.parent.ui.change_audio_value_from_box.text()), 3)
            toValue = round(float(self.parent.ui.change_audio_value_to_box.text()), 3)
            value = round(float(self.parent.ui.change_audio_value_box.text()), 3)
            if not isThereAnySelection:
                plotContainer[self.selectedPlot].setIndiceValueFromTo(None, fromValue, toValue, value)
                plotContainer[self.selectedPlot].setAmplitudeAndShift(shouldChangeROIminmax=True)
                self.showAudioWave(shouldUpdateAll=True)
                if plotContainer[self.selectedPlot].should_synq_with_mediator:
                    self.sendGraphToMediator(self.selectedPlot, True)
            else:
                #for plotCurve in plotContainer:
                plotContainer[self.selectedPlot].setIndiceValueFromTo(None, fromValue, toValue, value)
                plotContainer[self.selectedPlot].setAmplitudeAndShift(shouldChangeROIminmax=True)
                self.showAudioWave(shouldUpdateAll=True)
                if plotContainer[self.selectedPlot].should_synq_with_mediator:
                    self.sendGraphToMediator(self.selectedPlot, True)

    def clicked_metronome_button(self, sender, event = None):
        if sender.objectName().startswith("metronome_trigger_over_value_increase_button"):
            self.metronomeOverValue = round(float(self.parent.ui.metronome_trigger_over_value_box.text()) + 0.01, 2)
            self.parent.ui.metronome_trigger_over_value_box.setText(str(self.metronomeOverValue))
        elif sender.objectName().startswith("metronome_trigger_over_value_decrease_button"):
            self.metronomeOverValue = round(float(self.parent.ui.metronome_trigger_over_value_box.text()) - 0.01, 2)
            self.parent.ui.metronome_trigger_over_value_box.setText(str(self.metronomeOverValue))
        elif sender.objectName().startswith("metronome_trigger_under_value_increase_button"):
            self.metronomeUnderValue = round(float(self.parent.ui.metronome_trigger_under_value_box.text()) + 0.01, 2)
            self.parent.ui.metronome_trigger_under_value_box.setText(str(self.metronomeUnderValue))
        elif sender.objectName().startswith("metronome_trigger_under_value_decrease_button"):
            self.metronomeUnderValue = round(float(self.parent.ui.metronome_trigger_under_value_box.text()) - 0.01, 2)
            self.parent.ui.metronome_trigger_under_value_box.setText(str(self.metronomeUnderValue))

        elif sender.objectName().startswith("metronome_trigger_over_value_box"):
            self.metronomeOverValue = round(float(self.parent.ui.metronome_trigger_over_value_box.text()), 2)
        elif sender.objectName().startswith("metronome_trigger_under_value_box"):
            self.metronomeUnderValue = round(float(self.parent.ui.metronome_trigger_under_value_box.text()), 2)

    def setShouldUseDeforumationParameter(self, check_box_object, new_value, mediator_communication_string, should_set_checkbox_state, send_mediator_communication_string_on_off = False, mediator_values_to_write = None, configType = None):
        #self.p = self.deforumation_settings.getSendConfig()
        try:
            if new_value != -1:
                setattr(self, mediator_communication_string, new_value)
                #self.p[mediator_communication_string] = new_value
                if configType == None:
                    self.deforumation_settings.writeDeforumSendValuesToConfig(mediator_communication_string, new_value)
                else:
                    if configType == "gui":
                        self.deforumation_settings.writeDeforumationGuiValuesToConfig(mediator_communication_string, new_value)
                    elif configType == "send":
                        self.deforumation_settings.writeDeforumSendValuesToConfig(mediator_communication_string, new_value)
                    elif configType == "receive":
                        self.deforumation_settings.writeDeforumReceiveValuesToConfig(mediator_communication_string, new_value)
            else:
                if mediator_communication_string in self.deforumation_settings.getSendConfig():
                    setattr(self, mediator_communication_string, self.deforumation_settings.getSendConfig()[mediator_communication_string])
            if send_mediator_communication_string_on_off:
                if getattr(self, mediator_communication_string):
                    self.deforumationnamedpipes.writeValue(mediator_communication_string, 1)
                else:
                    self.deforumationnamedpipes.writeValue(mediator_communication_string, 0)
            #Communicate values to the mediator, if neccessary
            if mediator_values_to_write != None:
                for parameter_name in mediator_values_to_write:
                    parameter_value = mediator_values_to_write[parameter_name]
                    self.deforumationnamedpipes.writeValue(parameter_name, parameter_value)

            if should_set_checkbox_state:
                check_box_object.setChecked(getattr(self, mediator_communication_string))
            self.deforumation_tools.propagateAllCheckboxes(check_box_object)
        except Exception as e:
            if self.parent.is_verbose:
                print("(setShouldUseDeforumationParameter), has not yet a value (" + str(mediator_communication_string) +"), in config, and don't know if checkbox should be checked or not.")

    def handleCheckBoxesMetronome(self, event, sender, original_component_name):
        if sender.isChecked():
            if original_component_name.startswith("metronome_trigger_over_value_checkbox"):
                self.shouldUseMetronomeOverValue = False
                self.showAudioWave(shouldUpdateAll=True)
            elif original_component_name.startswith("metronome_trigger_under_value_checkbox"):
                self.shouldUseMetronomeUnderValue = False
                self.showAudioWave(shouldUpdateAll=True)
            elif original_component_name.startswith("metronome_trigger_cadence_value_checkbox"):
                self.shouldOnlyBeepOnCadence = False
        else:
            if original_component_name.startswith("metronome_trigger_over_value_checkbox"):
                self.shouldUseMetronomeOverValue = True
                self.metronomeOverValue = round(float(self.parent.ui.metronome_trigger_over_value_box.text()), 2)
                self.showAudioWave(shouldUpdateAll=True)
            elif original_component_name.startswith("metronome_trigger_under_value_checkbox"):
                self.shouldUseMetronomeUnderValue = True
                self.metronomeOverValue = round(float(self.parent.ui.metronome_trigger_under_value_box.text()), 2)
                self.showAudioWave(shouldUpdateAll=True)
            elif original_component_name.startswith("metronome_trigger_cadence_value_checkbox"):
                self.shouldOnlyBeepOnCadence = True

    def sendGraphToMediator(self, plot, should_use, should_write_status_to_plot = False):
        plotContainer = self.audioDataContainer.getPlots()
        if plot in plotContainer:
            if should_use:
                if should_write_status_to_plot:
                    plotContainer[plot].should_synq_with_mediator = True
                self.deforumationnamedpipes.writeValue("deforumation_graph_xshift", [plot, plotContainer[plot].currentXShift])
                self.deforumationnamedpipes.writeValue("should_use_deforumation_graph", [plot, 1])
                yAxisValues = plotContainer[plot].getYaxis().tolist()

                y_data = plotContainer[plot].getYaxis()
                x_data = plotContainer[plot].getXaxis()
                x_data_original = plotContainer[plot].getXaxisOriginal()
                f = interp1d(x_data, y_data, kind='linear')
                new_y_data = []
                for n in x_data_original:
                    x_val = f(n).tolist()
                    new_y_data.append(x_val)

                self.deforumationnamedpipes.writeValue("set_deforumation_graph", [plot, new_y_data])
            else:
                if should_write_status_to_plot:
                    plotContainer[plot].should_synq_with_mediator = False
                self.deforumationnamedpipes.writeValue("should_use_deforumation_graph", [plot, 0])
            return 0
        return -1

    def handleCheckBoxesGraphSynq(self, event, sender, original_component_name):
        if sender.isChecked():
            if original_component_name.startswith("audio_synq_strength_deforum_checkbox"):
                self.sendGraphToMediator("Strength", False, True)
            elif original_component_name.startswith("audio_synq_zoom_deforum_checkbox"):
                self.sendGraphToMediator("Zoom", False, True)
            elif original_component_name.startswith("audio_synq_panlr_deforum_checkbox"):
                self.sendGraphToMediator("PanLR", False, True)
            elif original_component_name.startswith("audio_synq_panud_deforum_checkbox"):
                self.sendGraphToMediator("PanUD", False, True)
            elif original_component_name.startswith("audio_synq_rotatev_deforum_checkbox"):
                self.sendGraphToMediator("RotateV", False, True)
            elif original_component_name.startswith("audio_synq_rotateh_deforum_checkbox"):
                self.sendGraphToMediator("RotateH", False, True)
            elif original_component_name.startswith("audio_synq_tilt_deforum_checkbox"):
                self.sendGraphToMediator("Tilt", False, True)
        else:
            if original_component_name.startswith("audio_synq_strength_deforum_checkbox"):
                ret = self.sendGraphToMediator("Strength", True, True)
                if ret == -1:
                    sender.setChecked(True)
            elif original_component_name.startswith("audio_synq_zoom_deforum_checkbox"):
                ret = self.sendGraphToMediator("Zoom", True, True)
                if ret == -1:
                    sender.setChecked(True)
            elif original_component_name.startswith("audio_synq_panlr_deforum_checkbox"):
                ret = self.sendGraphToMediator("PanLR", True, True)
                if ret == -1:
                    sender.setChecked(True)
            elif original_component_name.startswith("audio_synq_panud_deforum_checkbox"):
                ret = self.sendGraphToMediator("PanUD", True, True)
                if ret == -1:
                    sender.setChecked(True)
            elif original_component_name.startswith("audio_synq_rotatev_deforum_checkbox"):
                ret = self.sendGraphToMediator("RotateV", True, True)
                if ret == -1:
                    sender.setChecked(True)
            elif original_component_name.startswith("audio_synq_rotateh_deforum_checkbox"):
                ret = self.sendGraphToMediator("RotateH", True, True)
                if ret == -1:
                    sender.setChecked(True)
            elif original_component_name.startswith("audio_synq_tilt_deforum_checkbox"):
                ret = self.sendGraphToMediator("Tilt", True, True)
                if ret == -1:
                    sender.setChecked(True)




    def handleCheckBoxesMisc(self, event, sender, original_component_name):
        if sender.isChecked():
            if original_component_name.startswith("cadence_audio_line_show_checkbox"):
                self.shouldShowCadenceLines = False
        else:
            if original_component_name.startswith("cadence_audio_line_show_checkbox"):
                self.shouldShowCadenceLines = True
        self.showAudioWave(shouldUpdateAll=True)

    def handleCheckBoxes(self, event, sender, original_component_name):
        plotContainer = self.audioDataContainer.getPlots()
        if original_component_name == "editable_curve_checkbox":
            if sender.isChecked():
                if self.selectedPlot in plotContainer:
                    self.setShouldUseDeforumationParameter(sender, False, original_component_name+"_"+self.selectedPlot, False, configType="gui")
                    plotContainer[self.selectedPlot].unSelectAllIndices()
                    plotContainer[self.selectedPlot].isEditable = False

            else:
                if self.selectedPlot in plotContainer:
                    self.setShouldUseDeforumationParameter(sender, True, original_component_name+"_"+self.selectedPlot, False, configType="gui")
                    plotContainer[self.selectedPlot].isEditable = True
        elif original_component_name == "show_curve_checkbox":
            if sender.isChecked():
                if self.selectedPlot in plotContainer:
                    self.setShouldUseDeforumationParameter(sender, False, original_component_name+"_"+self.selectedPlot, False, configType="gui")
                    plotContainer[self.selectedPlot].unSelectAllIndices()
                    plotContainer[self.selectedPlot].isVisible = False

            else:
                if self.selectedPlot in plotContainer:
                    self.setShouldUseDeforumationParameter(sender, True, original_component_name+"_"+self.selectedPlot, False, configType="gui")
                    plotContainer[self.selectedPlot].isVisible = True
                    self.graphWidget.viewBox.change_points_colors([], plotContainer[self.selectedPlot])


        self.showAudioWave(shouldUpdateAll= True)

    def setComponetValues(self):
        plotContainer = self.audioDataContainer.getPlots()
        for plotCurve in self.availablePlots:
            if plotCurve in plotContainer:
                valueVisible = self.deforumation_settings.getGuiConfigValue("show_curve_checkbox_"+plotCurve)
                if valueVisible == None:
                    valueVisible = False
                plotContainer[plotCurve].isVisible = valueVisible
                valueEditable = self.deforumation_settings.getGuiConfigValue("editable_curve_checkbox_"+plotCurve)
                if valueEditable == None:
                    valueEditable = False
                plotContainer[plotCurve].isEditable = valueEditable

                plotColor = self.deforumation_settings.getGuiConfigValue(plotCurve+"_color")
                if plotColor != None:
                    plotColor = QColor(plotColor)
                    plotContainer[plotCurve].setPlotColor(plotColor)

                # Set the current selected plot values
                val = self.deforumation_settings.getGuiConfigValue(plotCurve + "_amplitude")  # Read from GuiConfig
                if val != None:
                    plotContainer[plotCurve].setAmplitudeAndShift(amplitude=val, shouldChangeROIminmax=True)

                val = self.deforumation_settings.getGuiConfigValue(plotCurve + "_shift")  # Read from GuiConfig
                if val != None:
                    plotContainer[plotCurve].setAmplitudeAndShift(shift=val, shouldChangeROIminmax=True)

                val = self.deforumation_settings.getGuiConfigValue(plotCurve + "_shiftleftright")  # Read from GuiConfig
                if val != None:
                    plotContainer[plotCurve].setAmplitudeAndShift(xshift=val, shouldChangeROIminmax=True)

                val = self.deforumation_settings.getGuiConfigValue(plotCurve + "_ampshift")  # Read from GuiConfig
                if val != None:
                    plotContainer[plotCurve].setAmplitudeAndShift(ampshift=val, shouldChangeROIminmax=True)

        if self.selectedPlot in plotContainer:
            self.parent.ui.show_curve_checkbox.setChecked(plotContainer[self.selectedPlot].isVisible)
            self.parent.ui.editable_curve_checkbox.setChecked(plotContainer[self.selectedPlot].isEditable)
            self.parent.ui.plot_color_button.setColor(plotContainer[self.selectedPlot].getPlotColor())

            #Set the current selected plot values
            val = self.deforumation_settings.getGuiConfigValue(self.selectedPlot + "_amplitude")  # Read from GuiConfig
            if val != None:
                self.parent.ui.amplitude_value_box.setText(str(val))
            else:
                self.parent.ui.amplitude_value_box.setText("-1")

            val = self.deforumation_settings.getGuiConfigValue(self.selectedPlot + "_shift")  # Read from GuiConfig
            if val != None:
                self.parent.ui.shift_value_box.setText(str(val))
            else:
                self.parent.ui.shift_value_box.setText("1")

            val = self.deforumation_settings.getGuiConfigValue(self.selectedPlot + "_shiftleftright")  # Read from GuiConfig
            if val != None:
                self.parent.ui.shift_leftright_value_box.setText(str(val))
            else:
                self.parent.ui.shift_leftright_value_box.setText("0")

            val = self.deforumation_settings.getGuiConfigValue(self.selectedPlot + "_ampshift")  # Read from GuiConfig
            if val != None:
                self.parent.ui.ampshift_value_box.setText(str(val))
            else:
                self.parent.ui.ampshift_value_box.setText("0")

            self.showAudioWave(shouldUpdateAll=True)


            # Set the correct color of the current plot
            if plotContainer[self.selectedPlot].isVisible:
                self.graphWidget.viewBox.change_points_colors([], plotContainer[self.selectedPlot])


    def setCurrentSelection(self, selectedPlot):
        self.selectedPlot = selectedPlot
        plotContainer = self.audioDataContainer.getPlots()
        if self.selectedPlot in plotContainer:
            amplitude_to_use = plotContainer[self.selectedPlot].getCurrentAmplitude()
            self.parent.ui.amplitude_value_box.setText(str(amplitude_to_use))

            shift_to_use = plotContainer[self.selectedPlot].getCurrentShift()
            self.parent.ui.shift_value_box.setText(str(shift_to_use))

            ampshift_to_use = plotContainer[self.selectedPlot].getCurrentAmpShift()
            self.parent.ui.ampshift_value_box.setText(str(ampshift_to_use))

            xshift_to_use = plotContainer[self.selectedPlot].getCurrentXShift()
            self.parent.ui.shift_leftright_value_box.setText(str(xshift_to_use))

    def currentSelectionChanged(self, index):
        self.selectedPlot = self.parent.ui.audio_plot_type.currentText()
        #print("Changed Plot to:" + self.selectedPlot)
        plotContainer = self.audioDataContainer.getPlots()
        if self.selectedPlot in plotContainer:
            self.parent.ui.editable_curve_checkbox.setChecked(plotContainer[self.selectedPlot].isEditable)
            self.parent.ui.show_curve_checkbox.setChecked(plotContainer[self.selectedPlot].isVisible)

            amplitude_to_use = plotContainer[self.selectedPlot].getCurrentAmplitude()
            self.parent.ui.amplitude_value_box.setText(str(amplitude_to_use))

            shift_to_use = plotContainer[self.selectedPlot].getCurrentShift()
            self.parent.ui.shift_value_box.setText(str(shift_to_use))

            ampshift_to_use = plotContainer[self.selectedPlot].getCurrentAmpShift()
            self.parent.ui.ampshift_value_box.setText(str(ampshift_to_use))

            xshift_to_use = plotContainer[self.selectedPlot].getCurrentXShift()
            self.parent.ui.shift_leftright_value_box.setText(str(xshift_to_use))

            plotColor = plotContainer[self.selectedPlot].getPlotColor()
            self.parent.ui.plot_color_button.setColor(plotColor)


    def setSpecialKey(self, keyName, onOff):
        if keyName == "Shift":
            self.setShiftKeyDown = onOff
        elif keyName == "Control":
            self.setControlKeyDown = onOff
        elif keyName == "a_key":
            if self.setControlKeyDown:
                plotContainer = self.audioDataContainer.getPlots()
                for plot in plotContainer:
                    if not plotContainer[plot].isVisible:  # or not plotContainer[plot].isEditable:
                        continue
                    print("Key ctrl-A was pressed")
                    self.graphWidget.viewBox.change_points_colors([], plotContainer[plot], selectAll=1)
        elif keyName == "c_key":
            if self.setControlKeyDown:
                self.graphWidget.viewBox.copyPointValues()
        elif keyName == "v_key":
            if self.setControlKeyDown:
                self.setControlV = True
                plotContainer = self.audioDataContainer.getPlots()
                lastIndiceIndex, lastIndiceIndex_original = plotContainer[self.selectedPlot].insertValuesFrom(self.copyBuffer, self.copyBuffer_x, self.copyBuffer_x_original, self.copyBuffer_modifiers)
                plotContainer[self.selectedPlot].setAmplitudeAndShift(shouldChangeROIminmax=True)

                plotContainer[self.selectedPlot].setSelectedIndices([lastIndiceIndex], selectedIndicesOriginal=[lastIndiceIndex_original])

                self.showAudioWave(shouldUpdateAll=True)
                self.setControlV = False
        elif keyName == "Alt":
            self.setAltKeyDown = onOff
        elif keyName == "Delete":
            plotContainer = self.audioDataContainer.getPlots()
            for plot in plotContainer:
                if not plotContainer[plot].isVisible:  # or not plotContainer[plot].isEditable:
                    continue
                #scatter = plotContainer[plot].getScatter()
                plotContainer[plot].addToRemovedVertices()
                #for plot in plotContainer:
                #    if not plotContainer[plot].isVisible:
                #        continue
                self.graphWidget.viewBox.change_points_colors([], plotContainer[plot])

                plotContainer[plot].setAmplitudeAndShift(shouldChangeROIminmax=True)
                self.showAudioWave(shouldUpdateAll=True)


    def togglePlayAudio(self):
        if self.audioDataContainer.shouldPlayAudio:
            self.audioDataContainer.shouldPlayAudioRememberPosition = False
            self.audioDataContainer.startPositionAudioPlayerStartPositionXaxis = self.audioDataContainer.currentAudioPlayerStartPositionXaxis
        self.audioDataContainer.shouldPlayAudio = not self.audioDataContainer.shouldPlayAudio

    def togglePlayAudioRememberStartPosition(self):
        self.audioDataContainer.shouldPlayAudioRememberPosition = True
        self.audioDataContainer.shouldPlayAudio = not self.audioDataContainer.shouldPlayAudio

    def currentTotalAudioVideoFrames(self):
        return self.audioDataContainer.currentTotalAudioVideoFrames

    def resetGraph(self):
        #print("Resetting graph.")
        plotContainer = self.audioDataContainer.getPlots()
        plotContainer[self.selectedPlot].chunk_modified_sample_data_amp_strength_modifiers = []
        plotContainer[self.selectedPlot].modified_sample_data_amp_strength_modifiers_removed_vertices = []
        plotContainer[self.selectedPlot].chunk_scatter_brushes = []
        #plotContainer[self.selectedPlot].expandPlot(20)
        plotContainer[self.selectedPlot].emptySelectedIndices()
        plotContainer[self.selectedPlot].setAmplitudeAndShift(shouldChangeROIminmax=True)
        self.showAudioWave(shouldUpdateAll=True)

    def deleteGraph(self):
        #print("Deleting graph.")
        self.resetGraph()
        plotContainer = self.audioDataContainer.getPlots()
        delList = (np.arange(len(plotContainer[self.selectedPlot].chunk_amplitudes)-2) + 1).tolist()
        plotContainer[self.selectedPlot].addToRemovedVertices(delList)
        highValue = plotContainer[self.selectedPlot].getIndiceValueHighAmp()
        lowValue = plotContainer[self.selectedPlot].getIndiceValueLowAmp()

        plotContainer[self.selectedPlot].chunk_amplitudes[0] = plotContainer[self.selectedPlot].calculateChunkAmplitudeFromCurrentValue(lowValue)
        plotContainer[self.selectedPlot].chunk_amplitudes[len(plotContainer[self.selectedPlot].chunk_amplitudes)-1] = plotContainer[self.selectedPlot].calculateChunkAmplitudeFromCurrentValue(highValue)
        plotContainer[self.selectedPlot].chunk_modified_sample_data_amp_strength_modifiers[0] = 0
        plotContainer[self.selectedPlot].chunk_modified_sample_data_amp_strength_modifiers[len(plotContainer[self.selectedPlot].chunk_modified_sample_data_amp_strength_modifiers)-1] = 0
        plotContainer[self.selectedPlot].emptySelectedIndices()


        plotContainer[self.selectedPlot].setAmplitudeAndShift(shouldChangeROIminmax=True)
        self.showAudioWave(shouldUpdateAll=True)

    def createAudioBeat(self):
        beat_value = float(self.parent.ui.audio_beat_value_box.text())
        other_value = float(self.parent.ui.audio_beat_value_other_box.text())
        number_of_beats_value = int(self.parent.ui.audio_number_of_beats_value_box.text())
        bpm_value = int(self.parent.ui.audio_bpm_value_box.text())
        plotContainer = self.audioDataContainer.getPlots()
        lastIndiceIndex, lastIndiceIndex_original = plotContainer[self.selectedPlot].insertBeatFrom(beat_value, other_value, number_of_beats_value, bpm_value)
        if lastIndiceIndex != -1:
            plotContainer[self.selectedPlot].setAmplitudeAndShift(shouldChangeROIminmax=True)
            plotContainer[self.selectedPlot].setSelectedIndices([lastIndiceIndex], selectedIndicesOriginal=[lastIndiceIndex_original])
            self.showAudioWave(shouldUpdateAll=True)
