# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:54:41 2017

@authors: emma, jona
"""

from direction import Direction
from collections import deque


class Snake(object):

    def __init__(self, max_x, max_y):
        self.body = deque()
        self.body.append((max_x // 2, max_y // 2))
        self.color = "blue"

    def grow(self, direction):
        (x, y) = self.body[-1]
        if direction == Direction.UP:
            y -= 1
        elif direction == Direction.DOWN:
            y += 1
        elif direction == Direction.LEFT:
            x -= 1
        else:
            x += 1
        self.body.append((x, y))

    def intersects_with_self(self):
        if len(self.body) == 1:
            return False
        else:
            x1, y1 = self.body[0]
            for i in range(1, len(self.body)):
                x2, y2 = self.body[i]
                if x1 == x2 and y1 == y2:
                    return True
            return False

    def move(self, direction):
        (x, y) = self.body[0]
        old = self.body.pop()
        if direction == Direction.UP:
            y -= 1
        elif direction == Direction.DOWN:
            y += 1
        elif direction == Direction.LEFT:
            x -= 1
        else:
            x += 1
        self.body.appendleft((x, y))
        return old, (x, y)
