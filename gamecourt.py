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

    def __init__(self, width, height, num_blocks):
        width = width
        height = height
        court = []

        self.master = Tk()
        self.master.title("Snake in Python")
        score_text = StringVar()
        Label(self.master, textvariable=score_text).pack()

        canvas = Canvas(self.master, width=width, height=height)
        canvas.pack()

        status_text = StringVar()
        Label(self.master, textvariable=status_text).pack()

        i = 0
        j = 0
        one_pixel = width // num_blocks
        while i < width:
            cols = []
            while j < height:
                cols.append(canvas.create_rectangle(i, j, i + one_pixel, j +
                                                    one_pixel, fill="white",
                                                    outline="white"))
                j = j + one_pixel
            court.append(cols)
            i = i + one_pixel
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
                status_text.set("Game over: You crashed against yourself!")
                self.button["state"] = "normal"
                return

            if x < 0 or y < 0 or x >= num_blocks or y >= num_blocks:
                status_text.set("Game over: You crashed against a wall!")
                self.button["state"] = "normal"
                return

            canvas.itemconfig(court[old_x][old_y], fill="white")

            if self.food_x == x and self.food_y == y:
                self.score += 1
                score_text.set("Score: {}".format(self.score))
                block = court[self.food_x][self.food_y]
                canvas.itemconfig(block, fill='white')
                self.snake.grow(self.direction)
                self.food_x = randint(0, num_blocks - 1)
                self.food_y = randint(0, num_blocks - 1)
                canvas.itemconfig(court[self.food_x][self.food_y], fill="red")

            for (x, y) in self.snake.body:
                canvas.itemconfig(court[x][y], fill=self.snake.color)

            self.master.after(100, update)
            return

        def reset():
            self.button["state"] = "disabled"
            for col in court:
                for block in col:
                    canvas.itemconfig(block, fill="white")
            self.snake = Snake(num_blocks, num_blocks)
            self.food_x = randint(0, num_blocks - 1)
            self.food_y = randint(0, num_blocks - 1)
            block = court[self.food_x][self.food_y]
            canvas.itemconfig(block, fill="red")
            self.direction = Direction.UP
            self.score = 1
            score_text.set("Score: 1")
            status_text.set("")
            self.master.after(0, update)

        self.master.bind("<Down>", down)
        self.master.bind("<Up>", up)
        self.master.bind("<Left>", left)
        self.master.bind("<Right>", right)

        self.button = Button(self.master, text="Try again", command=reset)
        self.button.pack()
        reset()

    def run(self):
        self.master.mainloop()
