# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 15:08:56 2022

@author: A Ramsey
"""
import numpy as np
from random import randint
import matplotlib.pyplot as plt

m = 8
n = 8

def possible_moves_at_beginning(m, n):
    '''
    Parameters
    ----------
    m : int
        horizontal dimension of board.
    n : int
        vertical dimension of board.

    Returns
    -------
    my_mat : numpy array
        matrix of number of possible moves from each square.
    '''
    my_mat = []
    rows = []
    for a in range(m):
        for b in range(n):
            count = 0
            for move in possible_moves:
                mo = [a + move[0], b + move[1]]
                if mo in coords(m, n):
                    count += 1
            rows.append(count)
        my_mat.append(rows)
        rows = []
    my_mat = np.array(my_mat)
    return my_mat

def coords(m, n):
    '''
    Parameters
    ----------
    m : int
        horizontal dimension of board.
    n : int
        vertical dimension of board.

    Returns
    -------
    all_coordinates : list
        list of all possible coordinates on m x n grid (index from zero).
    '''
    all_coordinates = []
    for a in range(m):
        for b in range(n):
            all_coordinates.append([a, b])
    
    return all_coordinates

all_coordinates = coords(m, n)

possible_moves = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]
chess_board = possible_moves_at_beginning(m, n)

def finds_knight_tour(m, n):
    '''
    Parameters
    ----------
    m : int
        horizontal dimension of board.
    n : int
        vertical dimension of board.

    Returns
    -------
    coords_list : list
        list of coordinates in order (assuming the path is successful).
    '''
    chess_board = possible_moves_at_beginning(m, n)
    x = randint(0, m - 1)
    y = randint(0, n - 1)
    coords_list = [[x, y]]
    
    while not np.array_equal(chess_board, np.zeros((m, n))):
        chess_board, x, y = one_turn(x, y)
        if x == "hello":
            break
        coords_list.append([x, y])
    
    if np.array_equal(chess_board, np.zeros((m, n))):
        return coords_list
    else:
        chess_board = possible_moves_at_beginning(m, n)
        return None
    
def one_turn(x, y):
    '''
    Parameters
    ----------
    x : int
        x coordinate.
    y : int
        y coordinate.

    Returns
    -------
    chess_board : numpy array
        board as it currently is (0s are places that have been used by knight).
    int
        new x coordinate.
    int
        new y coordinate.
    '''
    chess_board[x, y] = 0
    moves = []
    
    for move in possible_moves:
        m = [x + move[0], y + move[1]]
        if m in all_coordinates:
            if chess_board[m[0], m[1]] != 0:
                moves.append(m)
    
    nums = []
    for m in moves:
        num = chess_board[m[0], m[1]]
        nums.append(num)
    
    if len(moves) == 0:
        return chess_board, "hello", "hello"
    
    best_move = moves[nums.index(min(nums))]
    return chess_board, best_move[0], best_move[1]


x = finds_knight_tour(m, n)
while not isinstance(x, list):
    chess_board = possible_moves_at_beginning(m, n)
    x = finds_knight_tour(m, n)
    
#print(x)
if x != None:
        
    data = list(zip(*x))
    for n in range(len(data)):
        data[n] = list(data[n])
            
    xs = data[0]
    ys = data[1]
        
    plt.plot(xs, ys, marker='.')
    plt.grid()
    plt.show()
        