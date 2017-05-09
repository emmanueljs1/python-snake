# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:56:11 2017

@authors: emma, jona
"""

import Tkinter as tk
import Canvas

class GameCourt(object):    
    
    def __init__(self):
        master = tk()
        court = Canvas(master, width=500, height=500)
        
        