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

canvas = Canvas(root, width=300, height=300, highlightbackground="black", highlightthickness=1)
canvas.pack()

def plotPoint(event):
	global noteDesign
	noteDesign = []

	for i in range(300):
		noteDesign.append([0] * 300)
		
	blueColor = "#0096FF"
	if ((event.x > 5 and event.x < 295) and (event.y > 5 and event.y < 295)):
		x1 = (event.x - 5)
		x2 = (event.x + 5)
		y1 = (event.y - 5)
		y2 = (event.y + 5)
		canvas.create_oval(x1, y1, x2, y2, fill = blueColor, outline="")
		for i in range(11):
			for j in range(11):
				noteDesign[x1 + i][y1 + j] = 1
	
root.bind('<B1-Motion>', plotPoint)

notesLabel = Label(root, text = "")
notesLabel.pack()

def checkNote():
	global noteDesign

	print(noteDesign)

	rowsToPop = []

	for i in range(len(noteDesign)):
		shouldBreak = True
		for j in range(len(noteDesign)):
			if (noteDesign[i][j] == 1):
				shouldBreak = False
		if shouldBreak == True:
			rowsToPop.append(i)
	
	for i in range(len(rowsToPop) - 1, 0, -1):
		noteDesign.pop(rowsToPop[i])

	columnToPopLeft = []
	columnToPopRight = []

	for i in range(len(noteDesign[0])):
		shouldBreak = True
		for j in range(len(noteDesign)):
			if (noteDesign[j][i] == 1):
				shouldBreak = False
		if shouldBreak == True:
			columnToPopLeft.append(i)
		else:
			break

	for i in range(len(noteDesign[0]) - 1, 0, -1):
		shouldBreak = True
		for j in range(len(noteDesign)):
			if (noteDesign[j][i] == 1):
				shouldBreak = False
		if shouldBreak == True:
			columnToPopRight.append(i)
		else:
			break

	print(columnToPopRight)
	print(columnToPopLeft)

	for j in range(len(noteDesign)):
		for i in range(len(columnToPopRight)):
			noteDesign[j].pop(columnToPopRight[i])

	for j in range(len(noteDesign)):
		for i in range(len(columnToPopLeft) - 1, 0, -1):
			noteDesign[j].pop(columnToPopLeft[i])
	
	# for i in range(len(noteDesign)):
	# 	line = ""
	# 	for j in range(len(noteDesign[0])):
	# 		line = line + str(noteDesign[i][j])
	# 	print(line)
	
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

root.mainloop()
