# DeforumationQT Version 0.1.3

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
   - [Windows](#installation-windows)
   - [Linux](#installation-linux)
   - [Manual Installation](#manual-installation)
3. [Trouble Shooting](#trouble-shooting)
4. [Mediator Arguments](#mediator-arguments)
5. [DeforumationQT Arguments](#deforumationqt-arguments)
6. [Deforum Arguments](#deforum-arguments)
7. [Running Deforumation with OSC](#running-deforumation-with-osc)
8. [Further Help](#further-help)

## Prerequisites
- Automatic1111: Install and read instructions at [Automatic1111 GitHub](https://github.com/AUTOMATIC1111/stable-diffusion-webui).
- Python version 3.10.x: Download from [Python.org](https://www.python.org/downloads/).

## Installation

### Installation Windows
1. Navigate to the "Deforum_Version" folder.
2. Choose the communication method:
   - "piped" folder: Uses named pipes (recommended for local Windows).
   - "socket" folder: Uses websockets.
   - "hybrid" folder: Auto-selects based on OS.
3. Copy "sd-webui-deforum" to the Automatic1111 "extensions" folder.
4. Restart Automatic1111 if it was running.
5. Run "runme_windows_named_pipes.bat" or "runme_windows_websockets.bat".

### Installation Linux
1. Go to the "Deforum_Version" folder.
2. Copy "sd-webui-deforum" from the “socket” folder to the Automatic1111 "extensions" folder.
3. Restart Automatic1111 if it was running.
4. Install xterm: `sudo apt install xterm`.
5. Run `source runme_linux_websockets.sh` or `./runme_linux_websockets.sh`.

### Manual Installation
1. Ensure Python 3.10.xx is installed.
2. For Linux: Follow the provided steps to install Python 3.10.
3. Activate the virtual environment:
   - Linux & MacOS: `source ./venv/bin/activate`
   - Windows: `.\venv\Scripts\activate.bat`
4. Install requirements:
   - Linux & MacOS: `python -m pip install -r requirements_linux.txt`
   - Windows: `python -m pip install -r requirements_win.txt`
5. Start the mediator: `python mediator.py`
6. In a new terminal, start Deforumation: `python deforumation.py`

## Trouble Shooting
- Linux error with Qt platform plugin "xcb":
  - Install libxcb-cursor0: `sudo apt-get install libxcb-cursor0`
  - Run `python deforumation.py`

## Mediator Arguments
- Change listening addresses and ports:
  - For external traffic from Deforum: `python mediator.py "--mediator_deforum_address 0.0.0.0 -mediator_deforum_port 8765"`
  - For traffic between Deforumation and the mediator: `python mediator.py "--mediator_deforumation_address 0.0.0.0 -mediator_deforum_port 8766"`

## DeforumationQT Arguments
- Change listening addresses and ports for DeforumationQT:
  - `python deforumation.py "--deforumation_address 0.0.0.0 -deforumation_port 8767 --mediator_address 127.0.0.1 --mediator_port 8766"`

## Deforum Arguments
- Modify communication settings in `.../sd-webui-deforum/scripts/deforum_helpers/deforum_mediator.cfg`.
- Default: `ws://127.0.0.1:8765`
- If removed, the “Hybrid” version uses named pipes.

## Running Deforumation with OSC
- Windows: Run “runme_windows_named_pipes_osc.bat” or “runme_windows_websockets_osc.bat”.
- Linux: Run “runme_linux_websockets_osc.sh”.
- Manually: `python deforumation.py "--use_osc –osc_port 5005"`
- Default OSC port: 5005.
- Example OSC client: See “test_osc_client.py” in the Example folder.

## Further Help
- Join our Discord server: [Deforumation Discord](https://discord.gg/rbKFVh9v87).
