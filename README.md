# Netflix Surround Audio Trick

<div align="center">
    <img src="icon.webp" width="200">
    <br>
    <img src="https://img.shields.io/github/actions/workflow/status/shotwn/netflix-surround-audio-trick/build.yml">
    <img src="https://img.shields.io/badge/python-3.12-blue">
    <img src="https://img.shields.io/badge/OS-Windows_10-blue">
    <img src="https://img.shields.io/badge/OS-Windows_11-blue">
</div>


## The Problem
In 2024 Netflix retired their native **Windows** application and started to use a Edge based web application (PWA). Eventhough previously Edge was able to play Netflix in 5.1 surround sound, during this time surround options dissapeared from audio options. 

Surround audio is still available if Dolby Atmos is enabled in the system, but not everyone has a Dolby Atmos supported decoder. In fact most of the people use onboard sound cards or simple usb sound cards which does not support Dolby Atmos.

## The Solution
A simple trick can be used to enable surround sound in Netflix. This trick requires to buy a license for Dolby Access application from Microsoft Store and enabling Dolby Atmos for headphones. This will enable the surround sound in Netflix and it will stay enabled even if Dolby Atmos for headphones is disabled afterwards.

### Manual Steps
1. Buy [Dolby Access](https://www.microsoft.com/en-us/p/dolby-access/9n0866fs04w8) from Microsoft Store if you did not buy it before.
2. Open Dolby Access and enable Dolby Atmos for headphones.
    - This converts any surround stream to a stereo stream with simulated surround sound. We will turn this off later to use the original surround sound.
3. Open Netflix PWA via shortcut or browser. 
4. You can now disable Dolby Atmos for headphones and still have surround sound option in supported titles in Netflix.

## Automagic Steps - This Software
This software is a VERY simple python script that automates the steps above. Enables Dolby Atmos for headphones, opens Netflix, waits for 10 seconds and disables Dolby Atmos for headphones.

### Requirements for the Software
Script still requires Dolby Access. But also requires Netflix PWA from Microsoft Store to automatically open Netflix.
- [Netflix PWA from Microsoft Store](https://www.microsoft.com/en-us/p/netflix/9wzdncrfj3tj)
- [Dolby Access from Microsoft Store](https://www.microsoft.com/en-us/p/dolby-access/9n0866fs04w8)

You can ***download `Netflix.Surround.Audio.Trick.exe` from the [latest release](https://github.com/shotwn/netflix-surround-audio-trick/releases/latest/).***

### Requirements for Python Script
- Previously mentioned requirements
- Python 3.12 or higher
- Required packages can be installed via `pip install -r requirements.txt`

### Usage
Simply download and run the executable or run the python script. 

### Disclaimer
This software is not affiliated with Netflix or Dolby. It is a simple automation tool for a trick that can be done manually. It is not intended to be used for piracy or any other illegal activities.

## Windows SmartScreen
If you are having trouble running the executable, you can bypass Windows SmartScreen by clicking "More Info" and "Run Anyway".

Executable is built within GitHub Actions and completely open source. You can check the source code and build it yourself if you want.