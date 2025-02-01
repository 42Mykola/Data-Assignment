#imports
import pandas as pd
import matplotlib as plt
from tkinter import *
from tkinter import ttk
import numpy as np
import customtkinter as ctk
import matplotlib.pyplot as plt

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


#Defining graph generation
def generate_type_graph():
    #Counting the number of Pokemon for each type is happening here. Function "value_counts()" counts each
    #instane of specific Type 1 in the corresponding row, and then uses ".add" to add values from the rows
    #with type 2. "Fill_value=0" makes sure that empty spots are countes as 0 in the equation.
    type_counts = fileread['Type 1'].value_counts().add(fileread['Type 2'].value_counts(), fill_value=0)

    #Dictionary of colors is created to correspond to each type.
    colors = {
        'Bug': '#4B81F5', #Actually Water
        'Fire': '#4F3425', #Actually Ground
        'Grass': '#4F433D', #Actually Rock
        'Electric': '#329118', #Actually Grass
        'Psychic': '#AEB0B1', #Actually Steel
        'Ice': '#2F0131', #Actually Dark
        'Dragon': '#C2F4FF', #Actually Flying
        'Dark': '#A49586', #Actually Normal
        'Fairy': '#995FB1', #Actually Psychic
        'Fighting': '#CE60F7', #Actually Bug
        'Rock': '#99AEAD', #Actually Ghost
        'Ghost': '#9DE742', #Actually Poison
        'Normal': '#FFE100', #Actually Electric
        'Poison': '#C22222', #Actually Dragon
        'Water': '#9AFCFF', #Actually Ice
        'Ground': '#D08844', #Actually Fighting
        'Steel': '#F395DD', #Actually Fairy
        'Flying': '#E15320', #Actually Fire
    }

    #Colours are assigned based on type to the bars.
    bar_colors = [colors[type_name] for type_name in type_counts.index]

    # Plot the data
    plt.figure(figsize=(10, 6))
    type_counts.sort_values(ascending=False).plot(kind='bar', color = bar_colors)
    plt.title('Number of Pokémon per Type')
    plt.xlabel('Type')
    plt.ylabel('Number of Pokémon')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def on_button_click(name, type1, type2,
                    hp, atk, defense,
                   spAtk, spDef, spd, gen, leg):

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

#Search bar functions and creation of buttons that corresponds to the pokemon
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

#Frame for Other Buttons
functionFrame = ctk.CTkFrame(searchFrame)
functionFrame.pack(fill="x")

#Graph buttons
graphButton = ctk.CTkButton(functionFrame,
                            command=generate_type_graph,
                            fg_color=Carmine,
                            hover_color=DarkPurple,
                            text="Graph")
graphButton.pack(side = "left", expand = True, padx = 5, pady = 5)
DiamondButton = ctk.CTkButton(functionFrame,
                            fg_color=Carmine,
                            hover_color=DarkPurple,
                            text="Diamond Graph")
DiamondButton.pack(side = "left", expand = True, padx = 5, pady = 5)
randomPokemonButton = ctk.CTkButton(functionFrame,
                            fg_color=Carmine,
                            hover_color=DarkPurple,
                            text="Random Pokemon")
randomPokemonButton.pack(side = "left", expand = True, padx = 5, pady = 5)

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

