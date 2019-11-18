"""GUI Widget Presentation: Widget Alignment
   Robert Vanderhost Jr
   ITN 160 Programming I
   11/16/2019"""


# Import guizero library
import guizero


# Create the widget that will contain the aligned text
app = guizero.App(title='GUI Widget Alignment', width=500, height=500)

# Set the alignment, size, and color for the "Top Alignment" text
top_alignment = guizero.Text(app, text='TOP ALIGNMENT', align='top')
top_alignment.text_color = 'crimson'
top_alignment.text_size = 15

# Set the alignment, size, and color for the "Bottom Alignment" text
bottom_alignment = guizero.Text(app, text='BOTTOM ALIGNMENT', align='bottom')
bottom_alignment.text_color = 'dark violet'
bottom_alignment.text_size = 15

# Set the alignment, size, and color for the "Left Alignment" text
left_alignment = guizero.Text(app, text='LEFT ALIGNMENT', align='left')
left_alignment.text_color = 'blue2'
left_alignment.text_size = 15

# Set the alignment and size for the "Right Alignment" text
right_alignment = guizero.Text(app, text='RIGHT ALIGNMENT', align='right')
right_alignment.text_size = 15

# Display the widget
app.display()
