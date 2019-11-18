from guizero import *


def main():
    app = App(title="My app", height=300, width=300, layout="grid")
    win = Window(app, title='light', height=300, width=300,layout="grid")
    box = Box(app, layout="grid", grid=[1,0])
    box2 = Box(win, layout="grid", grid=[1,0])
    text = Text(app, text="Some text here", grid=[2,0])
    button1 = PushButton(win,text="1",height=10, width=10,grid=[0,0])
    button1 = PushButton(win,text="1",height=10, width=10,grid=[1,0])
    button1 = PushButton(win,text="1",height=10, width=10,grid=[2,0])
    waffle = Waffle(app, dim=10, color="green", width=8, height=8,grid=[0,0])
    waffle = Waffle(app, dim=10, color="green", width=8, height=8,grid=[1,0])
    waffle = Waffle(app, dim=10, color="green", width=8, height=8, grid=[0, 1])
    waffle = Waffle(app, dim=10, color="green", width=8, height=8, grid=[1, 1])
    app.display()
main()