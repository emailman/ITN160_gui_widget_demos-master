# Logan Smith
# 11-15-19
# ITN-160
# From github guizero on example on listbox

from guizero import *


def change_color(value):
    t.text_color = value


a = App()

t = Text(a, text="Its a ListBox", color="black")

listbox = ListBox(
    a,
    items=["red", "green", "blue", "yellow", "purple", "turquoise", "pink", "orange", "black", "brown", "cyan", 'white',
           'tan', 'teal', 'ivory'],
    selected="black",
    command=change_color,
    scrollbar=True)

a.display()
