First Parking Basement LED Display
=====================

This Python application displays traffic signs with associated countdown values in a fullscreen Pygame window. 
It is designed to be used as a visual display system in a parking or traffic management setup. 
Each image is shown alongside a countdown number, which decreases every 3 seconds. 
When the count reaches zero, an alternate "No Parking" image is displayed in place of the number.

Features
--------
- Fullscreen dynamic countdown display.
- Grid layout for 3x2 image-number pairs.
- Automatically loads images from a folder.
- Replaces numbers with a custom "zero-count" image when the timer runs out.

Prerequisites
-------------
- Python 3.x
- pygame module

Install pygame using pip if you haven't already:
    pip install pygame

File Structure
--------------
project-folder/
                │
                ├── Traffic Signs/                        # Folder containing all traffic sign images (PNG)

                │   ├── sign1.png

                │   ├── sign2.png

                │   └── ...

                │
                ├── 6.6 First Parking_No Parking Sign.png # Used when count reaches zero

                │
                └── version_6.py                               # The Python script

Note:
- The script uses up to 6 images from the Traffic Signs folder.
- Ensure that the zero-count image path in the script points to the correct location.

Running the Script
------------------
From your terminal or command prompt, navigate to the project directory and run:
    python version_6.py

The script will open in fullscreen mode. To exit, press any key or close the window.

Configuration
-------------
You can customize:
- Starting countdown values (see the line with: count = 10 + i * 2)
- Countdown interval (currently set to 3 seconds)
- Font and color schemes (editable near the top of the script)

License
-------
This project is intended for internal demonstration or signage use. 
Feel free to adapt it to your own parking or traffic management solutions.
"""
