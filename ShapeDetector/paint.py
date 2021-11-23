# Paint program template by https://gist.github.com/nikhilkumarsingh/85501ee2c3d8c0cfa9d1a27be5781f06
import os
from tkinter import *
from tkinter.colorchooser import askcolor
from PIL import Image

from ShapeDetector import shape_detection


class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.brush_button = Button(self.root, text='brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=0)

        self.color_button = Button(self.root, text='color', command=self.choose_color)
        self.color_button.grid(row=0, column=1)

        self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=2)

        self.save_button = Button(self.root, text='save', command=self.save)
        self.save_button.grid(row=0, column=3)

        self.c = Canvas(self.root, bg='white', width=600, height=400)
        self.c.grid(row=1, columnspan=4)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = 5.0
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.brush_button
        self.activate_button(self.brush_button)
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = 20.0 if self.eraser_on else 5.0
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def save(self):
        self.c.postscript(file = os.path.join(os.path.dirname(__file__), 'Drawings/savedImage.eps'), colormode='color')
        img = Image.open(os.path.join(os.path.dirname(__file__), 'Drawings/savedImage.eps'))
        img.save(os.path.join(os.path.dirname(__file__), 'Drawings/savedImage.png'), 'png')
        shape_detection.findShapes()
