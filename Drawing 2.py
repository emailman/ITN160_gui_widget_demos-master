'''
Zora Johnson
ITN 160
Guizero Widget Project
'''

from guizero import App, Text
app = App()
text = Text(app, text="Hey Everyone")
text = Text(app, text = "hi")
text.text_color = "green"

from guizero import App, Drawing
app = App()
drawing = Drawing(app)
drawing.rectangle(10, 10, 60, 60, color="purple")

app.display()

app.display()


