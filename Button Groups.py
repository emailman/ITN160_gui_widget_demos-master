from guizero import *
app = App()
choice = ButtonGroup(app, options=["options", "pcikme", "value"], selected="value")
app.display()