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

button = ctk.CTkButton(app, text="The Button™", fg_color=Button)
button.pack()

app.mainloop()
