# Piano-Sequencer
Type in a song and let the magic unfold!  
### Python Modules Used:
sounddevice, numpy, os, sys, time  
Note that if sounddevice or numpy isn't installed, the program will attempt to fix it by installing them via pip.  
  
Sounddevice requires the libportaudio2 package. This can be installed on Debian based distros with  
  
`sudo apt install libportaudio2`   
  
and on Fedora with  
  
`sudo dnf install portaudio-devel`  
### How to use: 
To type one note, type the note followed by the time period. Use '!' or '^' to play a lower or a higher octave respectively.  
Use Capital letters for sharp notes (Flat keys are NOT used in this sequencer).  
Separate each note by a space.  
Example: c4 c!4 C1 c^2.  
Here, c4 is a 4-beat C major note in the middle octave, c!4 is a 4 beat C major note in the lower octave.
### Saving and running songs in the sequencer:
You can also save and run songs directly using the sequencer. Enter the bpm and type in the song like you normally would to play it. Enter a name for it and it is now saved.
To run a song, simply type in the name of the song you used to save it.
##### Note:
The files are saved in .txt format in "Piano_Sequencer" where the py file is located. Just paste the path in a file explorer or use a terminal.
## Changelog:
Full changelog can be found [here](https://github.com/svta-7125/Piano-Sequencer/blob/Linux/changelog.md).
## Downloads and compatibility:
Download one of the files and run it using python3 or simply python. You can also make a sh script and run it as an executable to run it with a click.  
## Updates:
The app is usually updated regularly. Make sure to stop by and check for the latest update.

