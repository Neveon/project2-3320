from tkinter import *
from PIL import Image, ImageTk

# We create the app, make a canvas, place the image on the canvas,
# then we can use the mouse to draw lines on the canvas

window = Tk()
window.geometry("600x600")

# We can set the name of the image that is in the
# same folder as this file
imageName = "alien.jpg"

# Obtains x,y coordinates


def set_x_y(e):
    global last_x, last_y
    last_x, last_y = e.x, e.y


def draw(e):
    global last_x, last_y
    canvas.create_line(
        (last_x, last_y, e.x, e.y),
        fill='green',
        width=4
    )
    last_x, last_y = e.x, e.y


canvas = Canvas(window, bg='black')
canvas.pack(anchor='nw', fill='both', expand=1)

# bind keys to functions
canvas.bind("<Button-1>", set_x_y)
canvas.bind("<B1-Motion>", draw)


image = Image.open(imageName)
image = image.resize((600, 600), Image.ANTIALIAS)

image = ImageTk.PhotoImage(image)
canvas.create_image(0, 0, image=image, anchor='nw')


window.mainloop()
