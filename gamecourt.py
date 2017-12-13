# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:56:11 2017

@authors: emma, jona
"""

from snake import Snake
from tkinter import Tk, Canvas, Toplevel, Message, Button
from direction import Direction
from random import randint


class GameCourt(object):

    def __init__(self):
        master = Tk()
        master.title("Snake in Python")
        width = 500
        height = 500
        px = 10
        pixels = width // px
        canvas = Canvas(master, width=width, height=height)
        canvas.pack()
        court = []
        self.popup = None
        self.reset_button = None

        i = 0
        j = 0
        while i < width:
            cols = []
            while j < height:
                cols.append(canvas.create_rectangle(i, j, i + px,
                                                    j + px, fill="white",
                                                    outline="white"))
                j = j + px
            court.append(cols)
            i = i + px
            j = 0

        def up(event):
            self.direction = Direction.UP

        def down(event):
            self.direction = Direction.DOWN

        def left(event):
            self.direction = Direction.LEFT

        def right(event):
            self.direction = Direction.RIGHT
            
        def popup(string):
            #self.popup = Toplevel()
            #self.popup.title("Update:")
            #msg = Message(self.popup, text=string)
            self.popup = Message(master,text=string)
            self.popup.pack()
            self.reset_button = Button(master, text="Reset", command=reset)
            self.reset_button.pack()

        def update():
            (old_x, old_y), (x, y) = self.snake.move(self.direction)
            
            if self.snake.intersects_with_self():
                popup("You crashed against yourself!")
                return

            food_x, food_y = self.food
            canvas.itemconfig(court[food_x][food_y], fill="red")

            if food_x == x and food_y == y:
                canvas.itemconfig(court[food_x][food_y], fill="white")
                self.snake.grow(self.direction)
                self.food = randint(0, pixels - 1), randint(0, pixels - 1)

            if x < 0 or y < 0 or x >= pixels or y >= pixels:
                popup("You crashed against a wall!")
                return

            canvas.itemconfig(court[old_x][old_y], fill="white")

            for (x, y) in self.snake.body:
                canvas.itemconfig(court[x][y], fill=self.snake.color)

            master.after(100, update)

        def reset():
            if self.popup is not None:
                self.popup.destroy()
                self.popup = None

            if self.reset_button is not None:
                self.reset_button.destroy()
                self.reset_button = None

            for col in court:
                for block in col:
                    canvas.itemconfig(block, fill="white")
            self.snake = Snake()
            self.food = randint(0, pixels - 1), randint(1, pixels - 1)
            self.direction = Direction.UP
            master.bind("<Down>", down)
            master.bind("<Up>", up)
            master.bind("<Left>", left)
            master.bind("<Right>", right)
            master.after(0, update)
            master.mainloop()

        reset()
