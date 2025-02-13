# importing required libraries
from tkinter import *
import pygame
import time

root = Tk()
root.title("Rhythm Player")

root.geometry("500x600")
pygame.mixer.init()

title=Label(root,text="Rhythm") 
title.pack(side=TOP,fill=X)

global notes
notes = []

#Add later
def addQuarter():
	notes.append(1)
	notesOutput = "Quarter "
	play_button.config(state = "normal")
	notesLabel.config(text = notesOutput)

def addEighth():
	notes.append(0.5)
	notesOutput = "Eigth "
	play_button.config(state = "normal")
	notesLabel.config(text = notesOutput)
	
def addSixteenth():
	notes.append(0.25)
	play_button.config(state = "normal")
	notesOutput = "Sixteenth "
	notesLabel.config(text = notesOutput)

global notesOutput

tempoLabel = Label(root, text="Tempo")
tempoLabel.pack()
tempoSlider = Spinbox(root, from_= 10, to= 140)
tempoSlider.pack()

canvas = Canvas(root, width=110, height=300, highlightbackground="black", highlightthickness=1)
canvas.pack()

counter = 0

noteDesign = []
for i in range(300):
    noteDesign.append([0] * 110)

def plotPoint(event):
    global noteDesign
    
    blueColor = "#0096FF"
    if ((event.x > 5 and event.x < 105) and (event.y > 5 and event.y < 295)):
        x1 = (event.x - 5)
        x2 = (event.x + 5)
        y1 = (event.y - 5)
        y2 = (event.y + 5)
    canvas.create_oval(x1, y1, x2, y2, fill = blueColor, outline="")
    for i in range(11):
        for j in range(11):
            noteDesign[y1 + i][x1 + j] = 1
	
root.bind('<B1-Motion>', plotPoint)

notesLabel = Label(root, text = "")
notesLabel.pack()

def checkNote(): 

    #Might implement later
    # rowsToPop = []

    # for i in range(len(noteDesign)):
    #     shouldBreak = True
    #     for j in range(len(noteDesign)):
    #         if (noteDesign[i][j] == 1):
    #             shouldBreak = False
    #     if shouldBreak == True:
    #         rowsToPop.append(i)

    # for i in range(len(rowsToPop) - 1, 0, -1):
    #     noteDesign.pop(rowsToPop[i])

    # columnToPopLeft = []
    # columnToPopRight = []
    # for i in range(len(noteDesign[0])):
    #     shouldBreak = True
    #     for j in range(len(noteDesign)):
    #         if (noteDesign[j][i] == 1):
    #             shouldBreak = False
    #     if shouldBreak == True:
    #         columnToPopLeft.append(i)
    #     else:
    #         break

    # for i in range(len(noteDesign[0]) - 1, 0, -1):
    #     shouldBreak = True
    #     for j in range(len(noteDesign)):
    #         if (noteDesign[j][i] == 1):
    #             shouldBreak = False
    #     if shouldBreak == True:
    #         columnToPopRight.append(i)
    #     else:
    #         break

    # for j in range(len(noteDesign)):
    #     for i in range(len(columnToPopRight)):
    #         noteDesign[j].pop(columnToPopRight[i])

    # for j in range(len(noteDesign)):
    #     for i in range(len(columnToPopLeft) - 1, 0, -1):
    #         noteDesign[j].pop(columnToPopLeft[i])

    addData(noteDesign)

addNote = Button(root, text = "Add Note", command = checkNote)
addNote.pack()

def play():
	global notes 
	pygame.mixer.music.load("/Users/joshuaoh/Downloads/2022_03_29_19_strong_beat.wav")
	tempoSlider.config(state = "disabled")
	play_button.config(state = "disabled")
	currentTempo = int(tempoSlider.get())
	for i in range(len(notes)):
		pygame.mixer.music.play()
		time.sleep(notes[i] * (60/currentTempo))
	tempoSlider.config(state = "normal")
	notes = []
play_button = Button(root, text="Play Song", command=play)
play_button.config(state = "disabled")
play_button.pack(pady=20)

def displayLists(input):
    for i in range(len(input)):
        line = ""
        for j in range(len(input[i])):
            line = line + str(input[i][j])
        print(line)

def addData(input):
    cleanedData = input

    cleanedWidth = len(cleanedData[0])
    proportions = []

    for i in range(len(cleanedData)):
        currentProportions = []
        currentData = cleanedData[i][0]
        currentCounter = 0
        for j in range(len(cleanedData[0])):
            if (currentData != cleanedData[i][j]):
                if currentCounter >= 3:
                    currentProportions.append([cleanedData[i][j], currentCounter / cleanedWidth])
                    currentCounter = 0
                    currentData = cleanedData[i][j]                    
            else:
                currentCounter += 1
        currentProportions.append([cleanedData[i][j], currentCounter / cleanedWidth])
        proportions.append(currentProportions)

    '''
    -   :    What Type
    +   :    New Line
    |   :    New Note

    '''

    with open("/Users/test/Desktop/RhythmPlayer/quarterNote.txt", "a") as f:
        line = ""
        for i in range(len(proportions)):
            for j in range(len(proportions[i])):
                line = line + str(proportions[i][j][0]) + "-" + str(proportions[i][j][1])
            line = line + "+"
        line = line + "|"
        f.write(line + "\n")

    canvas.delete("all")

root.mainloop()
