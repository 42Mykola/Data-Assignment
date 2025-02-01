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



#defining on button click option
resultStat = 0
def on_button_click(name, type1, type2,
                    hp, atk, defense,
                   spAtk, spDef, spd, gen, leg):
    resultStat = name, type1, type2, hp, atk, defense, spAtk, spDef, spd, gen, leg
    print(resultStat)

    #Clears the details Frame widget for new stats to be set
    detailsFrame.delete("1.0", "end")

    #Inserts the stats of the pokemon that has been clicked on into the detailsFrame
    detailsFrame.insert("1.0",
                        f"Name: {name}"
                        f"\nType 1: {type1}"
                        f"\nType 2: {type2}"
                        f"\nHP: {hp}"
                        f"\nAttack: {atk}"
                        f"\nDefense: {defense}"
                        f"\nSp. Atk: {spAtk}"
                        f"\nSp. Def: {spDef}"
                        f"\nSpeed: {spd}"
                        f"\nGeneration: {gen}"
                        f"\nLegendary: {leg}")


#Defining the function for erasing the widgets when I need it
def remove_pokemon_():
    for widget in frameButtons.winfo_children():
        widget.destroy()

#Search bar functions and allat
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
        # row.get is used because some pokemon don't have a second type to them
        # and python refuses to work if you use row function and nothing appears
        type2 = row.get("Type 2", None)
        hp = row["HP"]
        atk = row["Attack"]
        defense = row["Defense"]
        spAtk = row["Sp. Atk"]
        spDef = row["Sp. Def"]
        spd = row["Speed"]
        gen = row["Generation"]
        leg = row["Legendary"]

        #Function for buttons that appear in response to type that has been searched
        button = ctk.CTkButton(frameButtons,
                               corner_radius=20, text=name, width=300,
                               text_color="white", fg_color= Carmine,
                               hover_color= DarkPurple,
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

#Frame for a search button, it fills the whole of x axis.
searchFrame = ctk.CTkFrame(app, fg_color=Timberwolf)
searchFrame.pack(fill="x")

#Frame for displaying Pokemon stats.
detailsFrame = ctk.CTkTextbox(app)
pokemonDetails = detailsFrame.insert("0.0", "Pokemon Details")
detailsFrame.pack(side="right", fill="y")

#Search bar frames
searchBar = ctk.CTkEntry(searchFrame, width= 500, fg_color= Ebony)
searchBar.pack(side= "left", padx= 5)
searchButton = ctk.CTkButton(searchFrame,
                             command=search_call,
                             fg_color= Carmine, text="Search",
                             hover_color= DarkPurple,)
searchButton.pack(side="right")

#Buttons of Pokemons that pop up when type is searched for.
frameButtons = ctk.CTkScrollableFrame(app)
frameButtons.pack(expand =True, fill="both", side="left")


#second button
#button2 = ctk.CTkButton(app, text="The Button 2™", fg_color=Button2)
#button2.place(x=70, y=70)
app.mainloop()


