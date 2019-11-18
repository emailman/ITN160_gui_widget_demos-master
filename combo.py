"""
ITN160 GUI Widget Assignment
Create a Widget for: Combo
11/11/19
"""
# What is a combo? A combo is a drop down box to select an item from.
# A combo is a list for you to pick from it can be as long as you want
# it to be.
# imports
from guizero import App, Combo, Text


# define the list
def animals(animal_pick):
    if animal_pick == "Cows":
        result.value = "\n\nMOO!!"
    elif animal_pick == "Ducks":
        result.value = "\n\nQUACK!!"
    elif animal_pick == 'Lions':
        result.value = "\n\nRAWR!!"
    elif animal_pick == "Tigers":
        result.value = "\n\nMEOW!!"
    elif animal_pick == "Bears":
        result.value = "\n\nOH MY!!!"


# build the GUI window
app = App(title='GUI Widget: Combo', height=200, width=200)
Text(app, "Choose an animal:", color='teal')

combo = Combo(app, options=["", "Cows", "Ducks", "Lions", "Tigers", "Bears"], command=animals)
result = Text(app)

app.display()
