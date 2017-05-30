# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:56:11 2017

@authors: emma, jona
"""

import snake
import Tkinter as tk

class GameCourt(object):    
    
    def __init__(self):
        self.master = tk.Tk()
        self.master.title("Snake in Python")
        
        self.canvas = tk.Canvas(self.master, width=500, height=500)
        
        self.court = []        
        
        i = 0
        j = 0        
        
        while i < 500:
            cols = []
            
            while j < 500:
                cols.append(self.canvas.create_rectangle(i, j, i + 10, j + 10, 
                    fill="white", outline="white"))
                j = j + 10
                
            self.court.append(cols)
            i = i + 10
            j = 0
                
        self.snake = snake.Snake()                 
                
        for (x, y) in self.snake.body:
            self.canvas.itemconfig(self.court[x][y], fill="blue")
                
        self.canvas.pack()
        self.master.mainloop()
        
        