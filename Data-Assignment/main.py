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

#Making python read the csv file
fileread = pd.read_csv('pokemon_data.csv')

#colours for tkinter
Wall1 = "#595A4A"             # #D0CFCF - Timberwolf  #595A4A - Ebony  #F6F7EB - Ivory  #331832 - Dark Purple  #A30015 - Carmine
Wall2 = "#D0CFCF"
Button = "#A30015"
Button2 = "#331832"
SearchBar = "#F6F7EB"


#The app itself and it's framing
app = ctk.CTk(fg_color=Wall1)
app.geometry("700x700")
app.title("Pokedex's Bizarre Adventure")
app.resizable(width=False, height=False)


#Fream for a search button, it fills the whole of x axis.
searchFrame = ctk.CTkFrame(app, fg_color=Wall2)
searchFrame.pack(fill="x")


#Search bar itself
searchBar = ctk.CTkEntry(searchFrame, width= 500, fg_color= SearchBar)
searchBar.pack(side= "left", padx= 5)


#Buttons of types of pokemons are displayed here
typeButtonFrame = ctk.CTkFrame(app, fg_color=Wall2)
typeButtonFrame.pack(anchor= "nw", padx= 5, pady= 5)


#Search Bar
def search_call():
    query = searchBar.get()  .





#definitions for finding by types

#Fire
def FindFire():
    print (fileread.loc[fileread['Type 1'] == "Fire"])
#Grass
def FindGrass():
    print (fileread.loc[fileread['Type 1'] == "Grass"])
#Water
def FindWater():
    print (fileread.loc[fileread['Type 1'] == "Water"])
#Ice
def FindIce():
    print (fileread.loc[fileread['Type 1'] == "Ice"])
#Bug
def FindBug():
    print (fileread.loc[fileread['Type 1'] == "Bug"])


#buttons
button = ctk.CTkButton(typeButtonFrame, text="Show Fire Type", fg_color=Button, command = FindFire)
button.pack()

button = ctk.CTkButton(typeButtonFrame, text="Show Grass Type", fg_color=Button, command = FindGrass)
button.pack()

button = ctk.CTkButton(typeButtonFrame, text="Show Water Type", fg_color=Button, command = FindWater)
button.pack()

button = ctk.CTkButton(typeButtonFrame, text="Show Ice Type", fg_color=Button, command = FindIce)
button.pack()

button = ctk.CTkButton(typeButtonFrame, text="Show Bug Type", fg_color=Button, command = FindBug)
button.pack()

#second button
#button2 = ctk.CTkButton(app, text="The Button 2™", fg_color=Button2)
#button2.place(x=70, y=70)
app.mainloop()


