
# 11/17/2019
# ITN 160
# Guizero Assignment

from guizero import *

from random import randint

# Create a list for all cards to be generated
Cards_Deck = ['SPADE', 'HEARTS', 'ACE', 'KING', 'QUEEN', 'JACK']


# Create a loop to be called upon to randomize the cards
def random_card():
    color = randint(1, 6)
    if color == 1:
        color = 'RED'
        print('RED SPADE')
    elif color == 2:
        color = 'YELLOW'
        print('YELLOW HEARTS')
    elif color == 3:
        color = 'GREEN'
        print('GREEN ACE')
    elif color == 4:
        color = 'BLUE'
        print('BLUE KING')
    elif color == 5:
        color = 'PURPLE'
        print('PURPLE QUEEN')
    elif color == 6:
        color = 'ORANGE'
        print('ORANGE JACK')
    return color


# Create an application and pushbuttons for the players
app = App(title='Card Generator', height=500, width=700)
PushButton(app, text='Draw Card', height=3, width=22, align="left", command=random_card)
left_writing = Text(app, text='Corey', align="left")
PushButton(app, text='Draw Card', height=3, width=22, align="right", command=random_card)
right_writing = Text(app, text='Shae', align="right")
PushButton(app, text='Draw Card', height=3, width=22, align="top", command=random_card)
top_writing = Text(app, text='Alex', align="top")
PushButton(app, text='Draw Card', height=3, width=22, align="bottom", command=random_card)
bottom_writing = Text(app, text='Zayn', align="bottom")

app.display()
