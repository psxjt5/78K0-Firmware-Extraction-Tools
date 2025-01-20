# 78K/0 Firmware Extraction Tools
Tools to extract the firmware from NEC 78K/0 Microcontrollers.

## 78K/0 Firmware Extraction (Assembler Source)
This file contains an assembly program that will output the contents of the entire memory map of a 78K/0.

The following pins are utilised:
- ```P120``` - Clock
- ```P50``` - Positional LSB
- ```P51``` - Positional MID
- ```P52``` - Positional MSB
- ```P53``` - Memory Data

Either the clock pin, or the positional outputs can be removed if a smaller number of output pins are required.

The output of these pins can be recorded by a Logic Analyser.

![6825b4f1-a73d-4028-b4fe-e02edb805a15](https://github.com/user-attachments/assets/fbf18e43-c0a0-47dc-801f-cf46ec88b499)

## 78K/0 Output Parser (Python Script)

This script takes the Logic Analyser output from Sigrok Pulseview, checks that the positional bits are sequencial, and then outputs the the firmware bits.

