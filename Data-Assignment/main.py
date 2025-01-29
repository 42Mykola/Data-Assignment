#imports
import pandas as pd
import matplotlib as plt
from tkinter import *
from tkinter import ttk
import numpy as np
import customtkinter as ctk

#making a main page
currentScene ="Main"

#Type is set as a default criteria for choosing pokemon
pokeChoice="Type"

#Changing search to Poke-type
searchpokemon = "Type"

#Making python read the csv file
fileread = pd.read_csv('pokemon_data.csv')

#colours for tkinter
Ebony = "#595A4A"
Timberwolf = "#D0CFCF"
Carmine = "#A30015"
DarkPurple = "#331832"
Ivory = "#F6F7EB"


#The app itself and it's framing
app = ctk.CTk(fg_color=Ebony)
app.geometry("700x700")
app.title("Pokedex's Bizarre Adventure")
app.resizable(width=False, height=False)


#Search Bar

def on_button_click(name, type1, type2,
                    hp, atk, defense,
                   spAtk, spDef, spd, gen, leg):
    print(name, type1, type2,
                                   hp, atk, defense,
                                   spAtk, spDef, spd, gen, leg)


def remove_pokemon_():
    for widget in frameButtons.winfo_children():
        widget.destroy()


def search_call():
    query = searchBar.get().strip().lower()
    filteredData=fileread[
                fileread['Type 1'].str.lower().str.contains(query) |
                fileread['Type 2'].str.lower().str.contains(query)
                ]
    filteredData = filteredData.drop_duplicates(subset=
    ['Name', 'Type 1', 'Type 2'])
    remove_pokemon_()
    for index, row in filteredData.iterrows():
        name = row["Name"]
        type1 = row["Type 1"]
        # row.get is used because some pokemon do not have a second type
        # and python doesn't like it if you use row[] and nothing appears
        type2 = row.get("Type 2", None)
        hp = row["HP"]
        atk = row["Attack"]
        defense = row["Defense"]
        spAtk = row["Sp. Atk"]
        spDef = row["Sp. Def"]
        spd = row["Speed"]
        gen = row["Generation"]
        leg = row["Legendary"]

        button = ctk.CTkButton(frameButtons,
                               corner_radius=20, text=name, width=300, text_color="white", fg_color= Carmine, hover_color= DarkPurple,
                               command=lambda
                                   name=name,
                                   type1=type1,
                                   type2=type2,
                                   hp=hp,
                                   atk=atk,
                                   defense=defense,
                                   spAtk=spAtk,
                                   spDef=spDef,
                                   spd=spd,
                                   gen=gen,
                                   leg=leg:
                               on_button_click(
                                   name, type1, type2,
                                   hp, atk, defense,
                                   spAtk, spDef, spd, gen, leg))
        button.pack(pady=5,anchor="w")

#Fream for a search button, it fills the whole of x axis.
searchFrame = ctk.CTkFrame(app, fg_color=Timberwolf)
searchFrame.pack(fill="x")


#Search bar itself
searchBar = ctk.CTkEntry(searchFrame, width= 500, fg_color= Ivory)
searchBar.pack(side= "left", padx= 5)
searchButton = ctk.CTkButton(searchFrame, command=search_call, fg_color= Carmine, text="Search", hover_color= DarkPurple,)
searchButton.pack(side="right")

frameButtons = ctk.CTkScrollableFrame(app)
frameButtons.pack(expand =True, fill="both", side="left")


#second button
#button2 = ctk.CTkButton(app, text="The Button 2™", fg_color=Button2)
#button2.place(x=70, y=70)
app.mainloop()


