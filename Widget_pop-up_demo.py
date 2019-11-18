"""Darius Sanders 
question pop-up demo
"""


from guizero import App, PushButton, Text


def ask():
    Quest = app.question ("Hello", "What's your name?")
    if Quest is not None:
        hello.value = "Sorry I don't care Mr." + Quest
        hello.size = 40
        hello.text_size = 30


app = App (title='Answer My Question', bg='green', width=1000, height=600)
btn = button = PushButton (app, command=ask, text="Hello")
btn.text_color = "yellow"
btn.text_size = 15
btn.height = 10
btn.width = 10
hello = Text (app, color='yellow')
app.display ()
