import os
from time import sleep
from sys import stdout
#import sounddevice as sd
os.system('clear')
try: import numpy as np
except: 
    print('numpy not found, installing')
    sleep(3)
    os.system('pip3 install numpy')
try: import sounddevice as sd
except: 
    print('sounddevice not found, installing')
    sleep(3) 
    os.system('pip3 install sounddevice')
flag1 = 1
if not os.path.isdir("Piano_Sequencer"): os.makedirs("Piano_Sequencer")
def Beep(frequency, duration_ms):   
    duration = duration_ms / 1000.0
    sample_rate = 44100
    time = np.linspace(0, duration, int(sample_rate * duration), False)
    waveform = np.sin(2 * np.pi * frequency * time)
    waveform /= np.max(np.abs(waveform))
    sd.play(waveform, sample_rate)
    sd.wait()
def scroller():
    a = '...................................'
    for char in a:
        stdout.write(char)
        stdout.flush()
        sleep(0.06)
def piano_engine(notes,bpm):
    notes_list = notes.split()
    Hz = 0
    for i in notes_list:
        valid = False
        ms = 0
        if len(i) == 2:
            freq = {'c':524,'C':555,'d':588,'D':623,'e':660,'f':699,'F':740,'g':784,'G':831,'a':880,'A':933,'b':988}
            for j in freq:
                if j == i[0]:
                    Hz = freq[j]
                    valid = True
            if i[0] not in freq: print("(Invalid Note given", i,")",end=" ")
        if len(i) == 3:
            freq = {'c!':262,'C!':278,'d!':294,'D!':312,'e!':330,'f!':350,'F!':370,'g!':392,'G!':415,'a!':440,'A!':467,'b!':494,'c^':1047,'C^':1109,'d^':1175,'D^':1245,'e^':1319,'f^':1397,'F^':1480,'g^':1568,'G^':1662,'a^':1760,'A^':1865,'b^':1976}
            for j in freq:
                if j == i[:2]:
                    Hz = freq[j]
                    valid = True
            if i[:2] not in freq: print("(Invalid Note given", i,")",end=" ")
        if bpm == 0:
            time = {'1':300,'2':600,'3':900,'4':1200}
            for j in time:
                if i[-1] == j:
                    ms = time[j]
            if ms == 0: print("(Invalid Time given", i,")",end=" ")
        if bpm >0:
            rate = 60000//bpm
            time = {'1':rate,'2':2*rate,'3':3*rate,'4':4*rate}
            for j in time:
                if i[-1] == j:
                    ms = time[j]
            if ms == 0: print("(Invalid Time given", i,")",end=" ")
        if flag1 == 1:
            if valid == True:
                stdout.write(i)
                print(end=" ")
                stdout.flush() 
        #Beep(Hz, ms)
        Beep(Hz,ms)         
def file(file_bpm, new_song, name):
    path = "Piano_Sequencer/"
    path += name
    full_text = str(file_bpm)+" "+new_song
    with open(path, 'w') as f: f.write(full_text)
    print("You can also find the files at \'%USERPROFILE%Piano_Sequencer/'.")
    print("Saving", end="")
    scroller()
    print("File Saved!")    
def run_file(name, notes):
    digit = ""
    for i in notes:
        if i.isnumeric() == True: digit+=i
        else:
            a = notes.index(i)
            break
    notes_final = notes[a+1::]
    piano_engine(notes_final, int(digit))    
def settings(setting_choice):
    global flag1
    if setting_choice == '1':
        if flag1 == 1: flag1 = 0
        elif flag1 == 0: flag1 = 1
        print("Changed")
''' if setting_choice == '1':
        print(\nEach letter and number represents a color:

        0 = Black       8 = Gray
        1 = Blue        9 = Light Blue
        2 = Green       A = Light Green
        3 = Aqua        B = Light Aqua
        4 = Red         C = Light Red
        5 = Purple      D = Light Purple
        6 = Yellow      E = Light Yellow
        7 = White       F = Bright White

Enter two characters, the first one represents the background color and the second one being the foreground color. 

        Examples: 2D, 5F, 70, ED
    
        Choose a background and text color:)
        clr = input()
        cmd = "color "+clr
        try: os.system(cmd)
        except: print("Failed")'''
print('''************************************************************************************************************************
******                                              Piano Sequencer v1.2.3                                        ******
*****************************************************************************************by svta-7125*******************


1)Enter notes and play song           2)Save a song            3)Edit an existing song

4)Run a song                          5)Delete a song          6)Open Settings

7)Show options                        8)Help                   9)Exit''')
while True:
    bpm = 0
    print('''


What would you like to do?
''')
    try: choice = int(input())
    except:
        print("Invalid input, try again.")
        continue
    if choice == 1:
        print("Enter bpm(0 for a default value)")
        try: bpm = int(input())
        except:
            print("Invalid BPM, try again")
            continue
        print("Enter your notes below")
        notes = input()
        print("\n")
        try: piano_engine(notes, bpm)
        except:
            print('Installing portaudio package')
            os.system('sudo apt install libportaudio2')
            os.system('sudo dnf install portaudio-devel')
            os.system('clear')
            print('Package installed for either Ubuntu or Fedora based Distros')
    elif choice == 2:
        print("Enter it's BPM, put 0 for a default value.")
        try: file_bpm = int(input())
        except:
            print("Invalid input, try again.")
            continue
        print("Enter your song to save!")
        new_song = input()
        print("What's the name of the song?")
        name = input() + '.txt'
        file(file_bpm, new_song, name)
    elif choice == 3:
        print("Enter the name of the file")
        name = input()
        name_mod = ""
        for i in name:
            if i == " ":
                i = "\ "
            name_mod+=i                    
        command = 'nano Piano_Sequencer/'+name_mod+'.txt'
        try:
            os.system(command)
        except:
            print("File does not exist, try again")
            continue
        os.system('nano Piano_Sequencer/'+name+'.txt')
    elif choice == 4:
        print("Enter the name of the file")
        name = input()
        print("\n")
        path = "Piano_Sequencer/" + name + '.txt'
        try:
            with open(path, 'r') as f:
                notes = f.readline()
        except:
            print("\nFile does not exist.")
            continue
        run_file(name, notes)
    elif choice == 5:
        print("Enter name of the song you want to delete")
        name = input()
        path = "Piano_Sequencer/" + name + '.txt'
        try: os.remove(path)
        except:
            print("\nFile doesn't exist, therefore, not deleted")
            continue
        print("Deleting", end = "")
        scroller()
        print("Deleted!")
    elif choice == 6:
        print("\nWhat would you like to change?")
        print('''1)Remove real-time note display''')
        setting_choice = input()
        try: int(setting_choice)
        except:
            print("Invalid option")
            continue
        settings(setting_choice)
    elif choice == 7:
        print('''
1)Enter notes and play song           2)Save a song            3)Edit an existing song

4)Run a song                          5)Delete a song          6)Open Settings

7)Show options                        8)Check for updates      9)Exit''')
    elif choice == 8:
        print('''
Welcome to the Piano Sequencer. Type your notes in order and let the song play!
To type one note, type the note followed by the time period. Use \'!\' or \'^\' to play lower or a higher octave.
Use Capital letters for sharp notes(No flat keys are used in this sequencer.).
Seperate each note by a space
Example: c4 c!4 C1 c^2''')    
    elif choice == 9:
        print("Thank you! Exiting", end = "")
        scroller()
        break
    elif choice == 69:
        print("\nCongratulations you found an easter egg! Here's a gift")
        file(200,"c1 c1 g1 g1 a1 a1 g2 f1 f1 e1 e1 d1 d1 c2 g1 g1 f1 f1 e1 e1 d2 g1 g1 f1 f1 e1 e1 d2 c1 c1 g1 g1 a1 a1 g2 f1 f1 e1 e1 d1 d1 c2", "Easter egg.txt")
        print( "File saved as: Easter egg")
    else:
        print("Invalid input, try again.")
        continue
