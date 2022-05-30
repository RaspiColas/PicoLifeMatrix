#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
    Game of life and matrix for Pico

"""

from random import randrange
from time import sleep
import picoscroll as scroll

debug = False


#----------------
# Gestion écran
#----------------

size_h = scroll.get_width()
size_v = scroll.get_height()


def cell_on(x, y, intensity):
    scroll.set_pixel(x, y, intensity)
    return


def cell_off(x, y):
    scroll.set_pixel(x, y, 0)
    return


def leds_display():
    scroll.update()
    return


def display_clear():
    scroll.clear()
    return


def display_text(text):
    scroll.scroll_text(text, 64, 80)
    return


def pressed():
    p = 0
    if scroll.is_pressed(scroll.BUTTON_X):
        p = 3
    elif scroll.is_pressed(scroll.BUTTON_Y):
        p = 4
    elif scroll.is_pressed(scroll.BUTTON_A):
        p = 1
    elif scroll.is_pressed(scroll.BUTTON_B):
        p = 2
    else:
        return 0
    sleep(1)
    
    if debug:
        print("p = %s" %(p))
        
    return p


#----------------
# Gestion cellules
#----------------

intensity_max = 32
gol_decr = 4
matrix_decr = 1.5

cell = {}
cell_1 = {}
for x in range(size_h):
    cell[x] ={}
    cell_1[x] = {}


def fill_zero():
    for x in range(size_h):
        for y in range(size_v):
            cell[x, y] = 0
            cell_1[x, y] = 0
    return


def cell_display():
    for x in range(size_h):
        for y in range(size_v):
            cell_on(x, y, cell[x, y])
    leds_display()
    return 


#----------------
# Gestion Jeu de la Vie
#----------------

def gol_fill_glider():
    cell[2, 3] = intensity_max
    cell[3, 4] = intensity_max
    cell[4, 2] = intensity_max
    cell[4, 3] = intensity_max
    cell[4, 4] = intensity_max
    return


def gol_fill_zero():
    for x in range(size_h):
        for y in range(size_v):
            cell[x, y] = 0
    return


def gol_fill_alea(r):
    for x in range(size_h):
        for y in range(size_v):
            if randrange(0, r) == 0:
                cell[x, y] = intensity_max
            else:
                cell[x, y] = 0
    return

    
def gol_init(r):
    fill_zero()
    if r == 1:
        gol_fill_glider()
    else:
        gol_fill_alea(r)
    return


def gol_neighbour(x, y):
    neighbour = 0
    for i in {-1, 0, 1}:
        for j in {-1, 0, 1}:
            if cell[(x+i) % size_h, (y+j) % size_v] == intensity_max:
                neighbour += 1
    return (neighbour)


def gol_cell_next_gen(x, y):
    neighbour = gol_neighbour(x, y)
    intensity = cell[x, y]
    
    if intensity == intensity_max:
        if (neighbour < 3) or (neighbour > 4):
            cell_1[x, y] = intensity // gol_decr
        else:
            cell_1[x, y] = intensity_max
    elif neighbour == 3:
        cell_1[x, y] = intensity_max
    else:
        cell_1[x, y] = intensity // gol_decr
    
    return


def gol_next_gen():
    for x in range(size_h):
        for y in range(size_v):
            gol_cell_next_gen(x, y)
            
    for x in range(size_h):
        for y in range(size_v):
            intensity = cell_1[x, y]
            cell[x, y] = intensity
            cell_on(x, y, intensity)
            
    return


def gameoflife(r):
    if debug:
        print("Jeu de la vie")
        
    gol_init(r)
    cell_display()
    
    g = 0
    while True:
        p = pressed()
        if p > 0:
            break
        gol_next_gen()
        leds_display()
        g += 1

    if debug:
        print("Generation: %s" %(g))
        
    return p


#----------------
# Gestion Matrix
#----------------

def matrix_next_gen():
    for col in range(size_h):
        for line in range(size_v-1, -1, -1):
            val = cell[col, line]
            cell[col, line] = int(val / matrix_decr)
            if line < randrange(0, size_h-1):
                cell[col, line + 1] = val
        if randrange(0, size_h) == 0:
            cell[col, 0] = 16
    return


def matrix():
    if debug:
        print("Matrix")
        
    fill_zero()

    while True:
        cell_display()
        p = pressed()
        if p > 0:
            break
        matrix_next_gen()
    return p


#----------------
# Main loop
#----------------

scroll.init()
display_clear()
    
while True:
    p = pressed()
    if p != 0:
        break
    sleep(0.1)

while True:
    if p == 4:
#        display_text("1 & 2 = GoL, 3 = Matrix")
        sleep(0.1)
        while True:
            p = pressed()
            if p != 0:
                break
            sleep(0.1)
    elif p == 3:
        p = matrix()
    else:
        p = gameoflife(p)



#-------------------------------------------------
#----- END OF THE PROGRAMME ----------------------
#-------------------------------------------------
