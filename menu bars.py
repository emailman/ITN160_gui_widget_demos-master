
# ITN 160
# Assignment 9
# Menu Bars

from guizero import *

waffle = None


def blue_function():
    waffle[0, 0].color = 'blue'
    print("color")


def green_function():
    waffle[0, 0].color = 'green'
    print("color")


def circle_function():
    waffle.dotty = True
    print("circle")


def square_function():
    waffle.dotty = False
    print("square")


def reset_function():
    waffle[0, 0].color = 'black'
    waffle.dotty = False
    print("reset")


def main():
    global waffle
    app = App()
    waffle = Waffle(app, height=1, width=1, color='black', dim=200)
    MenuBar(app,
            toplevel=["Color", "Shape", "Reset"],
            options=[
                [["Blue", blue_function], ["Green", green_function]],
                [["Circle", circle_function], ["Square", square_function]],
                [["Reset", reset_function]]
            ])

    app.display()


main()
