# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:56:11 2017

@authors: emma, jona
"""

from snake import Snake
from tkinter import Tk, Canvas, Button, Label, StringVar
from direction import Direction
from random import randint


class GameCourt(object):

    def __init__(self):
        width = 500
        height = 500
        px = 10
        pixels = width // px
        court = []

        master = Tk()
        master.title("Snake in Python")
        score_text = StringVar()
        Label(master, textvariable=score_text).pack()

        canvas = Canvas(master, width=width, height=height)
        canvas.pack()

        status_text = StringVar()
        Label(master, textvariable=status_text).pack()

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

        def update():
            (old_x, old_y), (x, y) = self.snake.move(self.direction)
            
            if self.snake.intersects_with_self():
                status_text.set("You crashed against yourself!")
                return

            food_x, food_y = self.food
            canvas.itemconfig(court[food_x][food_y], fill="red")

            if food_x == x and food_y == y:
                self.score += 1
                score_text.set("Score: {}".format(self.score))
                canvas.itemconfig(court[food_x][food_y], fill="white")
                self.snake.grow(self.direction)
                self.food = randint(0, pixels - 1), randint(0, pixels - 1)

            if x < 0 or y < 0 or x >= pixels or y >= pixels:
                status_text.set("You crashed against a wall!")
                return

            canvas.itemconfig(court[old_x][old_y], fill="white")

            for (x, y) in self.snake.body:
                canvas.itemconfig(court[x][y], fill=self.snake.color)

            master.after(100, update)

        def reset():
            for col in court:
                for block in col:
                    canvas.itemconfig(block, fill="white")
            self.snake = Snake()
            self.food = randint(0, pixels - 1), randint(1, pixels - 1)
            self.direction = Direction.UP
            self.score = 1
            score_text.set("Score: 1")
            status_text.set("Status: playing")
            master.bind("<Down>", down)
            master.bind("<Up>", up)
            master.bind("<Left>", left)
            master.bind("<Right>", right)
            master.after(0, update)
            master.mainloop()

        Button(master, text="Reset", command=reset).pack()
        reset()
