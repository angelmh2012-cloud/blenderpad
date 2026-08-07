

# BlenderPad

BlenderPad is a custom macropad project built for Blender workflow shortcuts, gaming controls, and a small OLED mini game. It is designed to be programmable with CircuitPython and KMK firmware, making it easy to customize for different use cases.
<img width="992" height="617" alt="Screenshot 2026-07-04 193833" src="https://github.com/user-attachments/assets/b69bbe3a-8599-4eee-a22d-8812ac43c819" />
## Project Overview
This project started as a beginner-friendly hardware and firmware build for HackClub. The goal is to create a compact keypad that can:
- trigger Blender shortcuts quickly
- switch between different key modes
- show the active mode on an OLED display
- support simple gaming-style input mappings

## What is included
This repository contains:
- a beginner-friendly 3D-printable case concept
- PCB design files
- firmware for the microcontroller
- a custom main script for mode switching and OLED output

## Hardware Features
The current design uses:
- an encoder for changing modes
- an OLED display for showing the active mode
- keys connected to GPIO pins for custom actions
- support for multiple functional profiles
  
<img width="558" height="446" alt="Screenshot 2026-07-13 210114" src="https://github.com/user-attachments/assets/259452dc-310b-485a-983f-e24993329a13" />
<img width="733" height="396" alt="Screenshot 2026-08-07 154843" src="https://github.com/user-attachments/assets/8c9715c7-21a9-45db-be12-7b12a253abd0" />


## Firmware Details
The firmware is written in Python and uses KMK for keyboard behavior. The device supports:
- Blender shortcuts mode
- Friday Night Funkin mode
- a mini game mode displayed on the OLED screen

## Pin Layout
- SDA: D4
- SCL: D5
- Encoder: D1
- Keys: D7 to D10

## Software Requirements
The firmware relies on the following Python libraries:
- adafruit-circuitpython-ssd1306
- adafruit-circuitpython-busdevice
- adafruit-circuitpython-framebuf

## How to Use It
1. Flash CircuitPython onto the microcontroller.
2. Copy the firmware files and required libraries to the device.
3. Upload the main script.
4. Power the board and test the keys and encoder.

<img width="542" height="395" alt="Screenshot 2026-07-13 210025" src="https://github.com/user-attachments/assets/d5b1c8cc-68ac-430b-98f0-5f68d00cb921" />

## Notes
This is a beginner project, so the design and firmware are still evolving. The main goal is to learn hardware programming, PCB design, and embedded firmware development in a fun and practical way.

## Future Ideas
Possible improvements include:
- adding more Blender shortcuts
- creating custom profiles for different programs
- improving the OLED mini game
- refining the case design for a cleaner final build

## Summary
BlenderPad is a fun, hands-on project that combines electronics, firmware, and creativity into one compact macropad. It is a great example of how small embedded projects can become useful tools for everyday tasks.


