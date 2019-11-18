from guizero import *

app = App(title='Python')

is_python = yesno('Is Python\n the best?', 'Is Python \nthe best?', app)

if is_python:
    app.info('Truth', 'You\'re right, it is!')

else:
    app.info('Falsehoods', 'Your opinion is wrong.')

app.display()
