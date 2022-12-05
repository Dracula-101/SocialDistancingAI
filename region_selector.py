# make a function that calls gui and returns the region

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os
from PIL import Image, ImageTk
from tkinter import Frame, Canvas

# make a function that opens a 800x800 window with a button
FRAME_HEIGHT = 500
FRAME_WIDTH = 600
region = 0


def generate_frame():
    top = tk.Tk()
    # make the resolution of the window 800x800
    top.geometry(f"{FRAME_WIDTH}x{FRAME_HEIGHT}")
    # make the window not resizable
    top.resizable(False, False)
    # change the background color to #292929
    top.configure(bg="#292929")
    # make the window title "Region Selector"
    top.title("Region Selector")
    # make a label that says "Region Selector"
    place_text("Region Selector", 30, 20, top, 30)
    # button = ttk.Button(top, text="Select Region", command=select_region)
    # # add the button to the window
    # button.place(x=50, y=100)

    # add image from assets folder
    load_image("assets/map1.png", 0, 100, top,
               int(FRAME_WIDTH/2), int(FRAME_WIDTH/2)-10)
    load_image("assets/map2.png", 300, 100, top,
               int(FRAME_WIDTH/2), int(FRAME_WIDTH/2)-10)
    # add two buttons
    add_button("Region 1", 100, 420, top,
               command=lambda: select_region1(top))
    add_button("Region 2", 400, 420, top,
               command=lambda: select_region2(top))
    # stop the widnow after pression the button
    top.mainloop()
    return region


def select_region1(top):
    global region
    region = 1
    top.destroy()


def select_region2(top):
    global region
    region = 2
    top.destroy()


def place_text(text, x, y, top, fontsize=12):
    label = tk.Label(top, text=text, bg="#292929",
                     fg="#FFFFFF", font=("Verdana", fontsize))
    label.place(x=x, y=y)
    top.update()


def load_image(path, x, y, top, height, width):
    photo_frame = Frame(top, height=height, width=width)
    photo_frame.pack()
    photo_frame.place(x=x, y=y)
    canvas = Canvas(photo_frame, height=height, width=width, bg="#292929")
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open(path).resize((height, width)))
    canvas.create_image(0, 0, anchor="nw", image=img)
    canvas.image = img
    top.update()


def add_button(text, x, y, top, command):
    button = ttk.Button(top, text=text, command=command)
    button.place(x=x, y=y)
    top.update()


if __name__ == '__main__':
    print(generate_frame())
