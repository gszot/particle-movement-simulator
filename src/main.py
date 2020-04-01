import pygame
import sys
from src.Board import Board
from src.Simulation import Simulation


r = 5                   #promien kulki
R = 500                 #'promień' pola
N = 70                  #ilość kulek
W = 8                   #losowanie prędkości z przedziału (-W,W)
acc = 0                #dokładnosc odbicia ( 0 -> 2r )
clockt = 60             #im więcej tym szybciej lecą

#pause/unpause dowolnym przyciskiem

board = Board(r, R, N, W, acc)
simulation = Simulation(board)
simulation.start()

