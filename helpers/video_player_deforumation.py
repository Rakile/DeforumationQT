import shutil
import sys
import time

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout, QSlider, QVBoxLayout, QWidget, QFileDialog
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QMediaMetaData
from PySide6.QtCore import Qt, QUrl, QTimer, QSize
from ui.ui_video_player import Ui_MainWindow

class Deforumation_Video_Player(QMainWindow):
    def __init__(self, parent, videoContainer, videoResolution):
        super().__init__()
        self.videoContainer = videoContainer
        self.parent = parent
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Deforumation Video Player")
        self.videoIsPaused = True
        self.isClosing = False
        self.videoResolution = videoResolution
        # Create a media player object
        self.mediaPlayer = QMediaPlayer()

        # Create an audio output object and set it to the media player
        self.audioOutput = QAudioOutput()
        self.mediaPlayer.setAudioOutput(self.audioOutput)
        # Connect the media player to the video widget
        self.mediaPlayer.setVideoOutput(self.ui.videoWidget)
        # Connect to the mediaPlayer's positionChanged and durationChanged signals
        self.mediaPlayer.positionChanged.connect(self.position_changed)
        self.mediaPlayer.durationChanged.connect(self.duration_changed)

        # Connect to the mediaStatusChanged signal
        # self.mediaPlayer.mediaStatusChanged.connect(self.onMediaStatusChanged)
        self.mediaPlayer.playbackStateChanged.connect(self.onPlaybackStateChanged)

        self.ui.play_button.clicked.connect(self.play_video)
        self.ui.paus_button.clicked.connect(self.pause_video)
        self.ui.slider.valueChanged.connect(self.set_position)

        self.ui.videoWidget.mouseReleaseEvent = self.mouseReleaseEvent_Image
        self.ui.restore_original_size.clicked.connect(self.resize_to_original_size)
        self.ui.save_video_to_file.clicked.connect(self.save_video_to_file)
        #self.load_video("H:/recordings/2023-12-07 08-05-04.mp4")
        #self.load_video("out.mp4")
        #self.ui.videoWidget.resize(VideoResolution)
        #rulle = self.size()
        #palle = self.ui.videoWidget.size()
        #self.play_video()
    def mouseReleaseEvent_Image(self, event):
        if self.videoIsPaused:
            self.play_video()
            #self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.pause_video()
            #self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def resizeDettachedPreviewWindow(self, event):
        current_preview_dettached_window_size = event.size()
        frameSize = self.videoResolution #self.ui.videoWidget.size()
        #framesizeScaledWidth = (frameSize.width() / frameSize.height()) * current_preview_dettached_window_size.height()
        framesizeScaledHeight = (frameSize.height() / frameSize.width()) * current_preview_dettached_window_size.width()
        shouldusethisheight = framesizeScaledHeight+self.extraBaggae  # int(frameSize.height() / 4)
        shouldusethiswidth = current_preview_dettached_window_size.width()   # in

        self.resize(QSize(shouldusethiswidth,shouldusethisheight))
        event.accept()
    def onPlaybackStateChanged(self, state):
        if state == QMediaPlayer.StoppedState:
            self.mediaPlayer.stop()
            #self.pause_video()
            #self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
            #print("Releasing the media file source")
            #self.mediaPlayer.setSource(QUrl())  # Release the media file source
            #print("Media file source has been released")
        #elif state == QMediaPlayer.StoppedState:
        #    print("Media stopped")

    """def onMediaStatusChanged(self, state):
        if self.isClosing and state == QMediaPlayer.StoppedState:
            self.mediaPlayer.setSource(QUrl())  # Release the media file source
            print("Release the media file source")
        elif QMediaPlayer.StoppedState:
            print("Media stopped")"""
    def setWindowSize(self, size):
        self.ui.videoWidget.resize(size)
        self.resize(size)

    def toggle_play_pause_video(self):
        if self.videoIsPaused:
            self.play_video()
        else:
            self.pause_video()
    def play_video(self):
        self.mediaPlayer.play()
        self.videoIsPaused = False
        #self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))

    def pause_video(self):
        palle = self.ui.videoWidget.size()
        palle = self.size()
        self.mediaPlayer.pause()
        self.videoIsPaused = True


        #self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def stop_video(self):
        self.mediaPlayer.stop()

    def set_position(self, position):
        was_playing = self.mediaPlayer.playbackState() == QMediaPlayer.PlayingState
        self.mediaPlayer.setPosition(position)
        if not was_playing:
            self.mediaPlayer.play()
            self.mediaPlayer.pause()

    def position_changed(self, position):
        self.ui.slider.blockSignals(True)
        self.ui.slider.setValue(position)
        self.ui.slider.blockSignals(False)

    def duration_changed(self, duration):
        self.ui.slider.setRange(0, duration)

    def load_video(self, url):
        #print("Loading video:", url)
        self.mediaPlayer.setSource(QUrl.fromLocalFile(url))
        #print("Video loaded")
        #self.videoResolution = self.mediaPlayer.metaData().data[self.mediaPlayer.metaData().Key.Resolution]
        self.videoPlayerHeight = self.videoResolution.height() + self.ui.play_button.height() + self.ui.slider.height() + 4
        self.extraBaggae = self.ui.play_button.height() + self.ui.slider.height() + 4
        self.resize(QSize(self.videoResolution.width(), self.videoPlayerHeight))
        self.resizeEvent = self.resizeDettachedPreviewWindow
    def resize_to_original_size(self, event = None):
        self.resize(QSize(self.videoResolution.width(), self.videoPlayerHeight))

    def save_video_to_file(self, event = None):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save Video File", "", "Video File(*.mp4)")
        if file_name != "" and file_name != None:
            shutil.copyfile("out.mp4", file_name)
            print("Video written to: ", file_name)

    def set_volume(self, value):
        # Convert the slider value to a float between 0.0 and 1.0
        volume_level = value / 100.0
        self.audioOutput.setVolume(volume_level)

    def closeEvent(self, event):
        #Begin with saving the video player window size and position for the next opening
        self.parent.saveFFMPEGpreviewWindowPosition(self)
        # Cleanup routine before the window is closed
        self.mediaPlayer.stop()
        time.sleep(0.1) # Need a delay, else setSource will freeze
        self.mediaPlayer.setSource(QUrl())
        self.mediaPlayer.deleteLater()
        self.videoContainer.occupied = False
        self.videoContainer.player = None
        event.accept()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Deforumation_Video_Player(None, QSize(512,512))
    widget.show()
    sys.exit(app.exec())