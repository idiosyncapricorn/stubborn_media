# stubborn_media

BPM-Synced Light Show

A Python program that plays an MP3 file and creates a full-screen light show synchronized to the song’s BPM with periodic strobe effects.

Features

	1.	BPM Analysis: Automatically calculates the song’s BPM using librosa.
	2.	Color Changes: Alternates colors (Pink, Turquoise, Mint Green, Gold) based on the BPM.
	3.	Strobe Effect: Flashes white and black every 15 seconds for 5 seconds.
	4.	Full-Screen Mode: Immersive visual experience.

Requirements

	•	Python 3.7+
	•	Libraries: librosa, pygame, numpy
	•	Install with:

pip install librosa pygame numpy

Usage

	1.	Place your MP3 file in the same folder as the script.
	2.	Run the script:

python main.py


	3.	Enter the path to your MP3 when prompted.
	4.	Press Esc to exit.

Customization

	•	Change colors in the colors list.
	•	Modify strobe timing in strobe_intervals.

Enjoy the light show! 🎶✨