# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 17:54:41 2017

@authors: emma, jona
"""

from gamecourt import GameCourt


def main():
    width = 500
    height = 500
    num_blocks = 50
    gc = GameCourt(width, height, num_blocks)
    gc.run()

if __name__ == '__main__':
    main()
