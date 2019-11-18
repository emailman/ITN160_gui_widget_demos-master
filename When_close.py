from guizero import *

# Ask the user if they really want to close the window
def do_this_when_closed():
    if app.yesno("Close", "Do you want to quit?"):
        app.destroy()

app = App()

info('test', 'this is test')
app.warn("test",'One attempt')
title = Text(app, text="test")

# When the user tries to close the window, run the function do_this_when_closed()
app.when_closed = do_this_when_closed

app.display()