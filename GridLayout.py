'''
Assignment 9 - GUI Widgets Presentation
11/17/19
'''

from guizero import *

# app = App(layout="grid", width=300, height=400)
app = App(layout="grid", width=500, height=500)

button1 = Picture(app, image="mailman/1.png", grid=[0, 0])
button2 = Picture(app, image="mailman/2.png", grid=[1, 0])
button3 = Picture(app, image="mailman/3.png", grid=[2, 0])
button4 = Picture(app, image="mailman/4.png", grid=[0, 1])
button5 = Picture(app, image="mailman/5.png", grid=[1, 1])
button6 = Picture(app, image="mailman/6.png", grid=[2, 1])
button7 = Picture(app, image="mailman/7.png", grid=[0, 2])
button8 = Picture(app, image="mailman/8.png", grid=[1, 2])
button9 = Picture(app, image="mailman/9.png", grid=[2, 2])
# button0 = Picture(app, image="mailman/0.png", grid=[1, 3])
button0 = Picture(app, image="mailman/0.png", grid=[0, 3])

# [x, y, xspan, yspan]
tall = Picture(app, image="mailman/tall.png", grid=[3, 0, 1, 2])
wide = Picture(app, image="mailman/wide.png", grid=[1, 3, 2, 1])

app.display()
