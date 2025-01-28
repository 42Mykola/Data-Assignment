#imports
import pandas as pd
import matplotlib as plt
from tkinter import *
from tkinter import ttk
import csv
import numpy as np
import customtkinter as ctk

#making a main page
currentScene ="Main"

#Changing search to Poke-type
searchpokemon = "Type"

#making python read the csv file
fileread = pd.read_csv('pokemon_data.csv')

#colours for tkinter
Wall1 = "#A30015"
Wall2 = "#BD2D87"
Button = "#D664BE"
Button2 = "#DF99F0"
SearchBar = "#B191FF"

app = ctk.CTk(fg_color=Wall1)
app.geometry("700x700")
app.title("Pokedex's Bizarre Adventure")
app.resizable(width=False, height=False)

displayScreen = Tk()

def FindFire():
    print (fileread.loc[fileread['Type 1'] == "Fire"])
    filteredData =

def FindGrass():
    print (fileread.loc[fileread['Type 1'] == "Grass"])

#first button
button = ctk.CTkButton(app, text="Show Fire Type", fg_color=Button, command = FindFire)
button.place(x=280, y=42)

button = ctk.CTkButton(app, text="Show Grass Type", fg_color=Button, command = FindGrass)
button.place(x=280, y=82)

#second button
#button2 = ctk.CTkButton(app, text="The Button 2™", fg_color=Button2)
#button2.place(x=70, y=70)
app.mainloop()

