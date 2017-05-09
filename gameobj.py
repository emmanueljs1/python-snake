# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:55:03 2017

@authors: emma, jona
"""

class GameObj(object) :    
    
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        
    # does this game object intersect with another game object    
    def intersects(self, go):
        return (go.x + go.width > self.x and 
                go.x < self.x + self.width and 
                go.y + go.height > self.y and 
                go.y < self.y + go.height)