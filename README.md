# PicoLifeMatrix

Pico Life Matrix is a MicroPython script for displaying game-of-life or matrix-style patterns on Pimoroni's PicoScroll installed on a Raspberry Pico

It requires to install pimoroni-pico-vXXX-micropython.uf2 (current version : v1.18.7) in the pico

Four options (selectable with the 4 buttons):
1- Start game-of-life with a "glider" (ie, en eternal pattern which reproduces itself accross the board)
2- Start game-of-life with a random pattern
3- Display matrix-like pattern
4- Freeze latest display

Note that a "feature" dims progressively the game-of-life cells from generation to generation (taking advantage of the fact that one can adjust individual led intensity on the picoscroll)
