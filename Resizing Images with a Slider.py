from guizero import *


# show the image window and resize it to have space for the full image
def show_image(image_win):
    global original_image_height, original_image_width
    image_win.show()
    image_win.height = original_image_height
    image_win.width = original_image_width


def resize_image(slider_value):
    global image, original_image_height, original_image_width

    # calculate new size of the image and resize the image accordingly
    new_image_height = int(original_image_height * int(slider_value) / 100)
    new_image_width = int(original_image_width * int(slider_value) / 100)
    image.resize(new_image_width, new_image_height)


# take image file name
image_file_name = 'img1.png'

# define main window and image window
main_window = App('Image resize', width=300, height=200)
image_window = Window(main_window, 'Resized Image', visible=False)

# add a push button (to main window) to show image
Box(main_window, height=30, width=30, align="top")   # add a margin at the top
PushButton(main_window, text='Show Image', command=show_image, args=[image_window])   # a button to show image

# add the image to image window
image = Picture(image_window, image=image_file_name)
original_image_height = image.height
original_image_width = image.width

# add a slider (to main window) that changes the size of the image based on the slider value (as a percentage)
Box(main_window, height=20, width=20, align="top")  # add a margin at the top
Text(main_window, text="Scale: ")
image_resize_slider = Slider(main_window, start=1, end=100, command=resize_image)
image_resize_slider.value = 100

# show main window
main_window.display()