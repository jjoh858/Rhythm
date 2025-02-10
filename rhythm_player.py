# importing required libraries
from tkinter import *
import pygame
import time

root = Tk()
root.title("Rhythm Player")

root.geometry("500x400")
pygame.mixer.init()# initialise the pygame

def addQuarter():
	notes.append(1)
	notesOutput = "Quarter "
	notesLabel.config(text = notesOutput)
	
def addEighth():
	notes.append(0.5)
	notesOutput =  "Eigth "
	notesLabel.config(text = notesOutput)

	
def addSixteenth():
	notes.append(0.25)
	notesOutput = "Sixteenth "
	notesLabel.config(text = notesOutput)

global notesOutput
notesLabel = Label(root, text = "")
notesLabel.pack()

global notes
notes = []

quarterNote = Button(root, text = "Quarter Note", command = addQuarter)

eightNote = Button(root, text = "Eighth Note", command = addEighth)

sixteenthNote = Button(root, text = "Sixteenth Note", command = addSixteenth)

eightNote.pack()
quarterNote.pack()
sixteenthNote.pack()

tempoSlider = Spinbox(root, from_= 10, to= 140)
tempoSlider.pack()

def play():
	pygame.mixer.music.load("/Users/joshuaoh/Downloads/2022_03_29_19_strong_beat.wav")
	tempoSlider.config(state = "disabled")
	currentTempo = int(tempoSlider.get())
	print(notes)
	for i in range(5):
		pygame.mixer.music.play()
		time.sleep(notes[i] * (60/currentTempo))
	tempoSlider.config(state = "normal")
	notes = []
	print(notes)
	
title=Label(root,text="Rhythm") 
title.pack(side=TOP,fill=X)

play_button = Button(root, text="Play Song", command=play)
play_button.pack(pady=20)
root.mainloop()
