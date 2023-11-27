# Piano-Sequencer
Type in a song and let the magic unfold!  
## ATTENTION:
A new linux port has been made, available in the Linux branch, based on version 1.2.1 beta.  
This is now the MAIN REPOSITORY SINCE THE OLD ACCOUNT GOT LOCKED OUT. *oops*
### Python Modules Used:
winsound (Works only on windows), os, sys, time
### How to use: 
To type one note, type the note followed by the time period. Use '!' or '^' to play lower or a higher octave respectively.  
Use Capital letters for sharp notes (Flat keys are NOT used in this sequencer).  
Separate each note by a space.  
Example: c4 c!4 C1 c^2.  
Here, c4 is a 4-beat C major note in the middle octave, c!4 is a 4 beat C major note in the lower octave.
### Saving and running songs in the sequencer:
You can also save and run songs directly using the sequencer. Enter the bpm and type in the song like you normally would to play it. Enter a name for it and it is now saved.
To run a song, simply type in the name of the song you used to save it.
##### Note:
The files are saved in .txt format in "%USERPROFILE%\Piano_Sequencer". Just paste the path in the search box or the run dialog box.
## Changelog:
Full changelog can be found here https://github.com/svta-7125/Piano-Sequencer/blob/main/changelog.md
## Downloads and compatibility:
Go to the release tab and download the latest release. Make sure you select the .exe file for download. 
  
All releases are tested in Windows 11 22H2 and should work in Windows 10 and Windows 11.  
Issues were found when running it in Windows 8.1 and Windows 7.  
Can run in linux distros using WINE(may not be audible).  
Linux port now availible in the linux branch.
## Updates:
The app is usually updated regularly. Make sure to stop by and check for the latest update.
## Build your own version of Piano Sequencer:
You can build your own executable using any one of the python files given above. Required modules are Pyinstaller. Use Auto-py-to-exe for a GUI.  
  
  
  Use 1229.ico for setting the icon pic for the final .exe

