# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 20:37:54 2022

@author: A Ramsey
"""

import matplotlib.pyplot as plt
import numpy as np
###
from matplotlib.collections import LineCollection
#from matplotlib.colors import ListedColormap, BoundaryNorm
###

xs = []
ys = []

possible_moves = [[1, 2], [-1, 2], [1, -2], [-1, -2], [2, 1], [-2, 1], [2, -1], [-2, -1]]
base = [[25, 10, 11, 12, 13], [24, 9, 2, 3, 14], [23, 8, 1, 4, 15], [22, 7, 6, 5, 16], [21, 20, 19, 18, 17]]
triangle_base = [[1, 3, 6], [2, 5, 9], [4, 8, 13]]
tb2 = [[1, 3], [2, 5]]
position = [2, 2]
tri_position = [0, 0]

def layer(board):
    '''
    Parameters
    ----------
    board : list
        list of lists (nxn matrix of numbers representing centre of spirally enumerated infinite chess board).

    Returns
    -------
    new_board : list
        board, but with one extra layer (nxn -> (n+2)x(n+2)).
    '''
    l = len(board) + 2
    new_board = []
    top_row = list(range((l-2)**2 + 1, (l-2)**2 + l))
    top_row.insert(0, l**2)
    bottom_row = list(reversed(list(range(top_row[-1] + l - 1, top_row[0] - l + 2))))
    new_board.append(top_row)
    
    for i in range(l-2):
        current_row = board[i]
        current_row.insert(0, l**2 - i - 1)
        current_row.append(top_row[-1] + i + 1)
        new_board.append(current_row)
        
    new_board.append(bottom_row)
    
    return new_board

def triangle_layer(board):
    l = len(board)
    new_row_start = board[l-1][0] + l
    new_row = [new_row_start]
    for i in range(l):
        new_row.append(new_row[i] + l + 2 + i)
    
    for b in board:
        b.append(b[-1] + (b[-1] - b[-2]) + 1)
        
    board.append(new_row)
    return board

def finds(list1, proper_val):
    '''
    Parameters
    ----------
    list1 : list
        list of lists we want to find a value in.
    proper_val : any type
        value we want to find in nested list.

    Returns
    -------
    x : list
        index of value.
    '''
    for a in list1:
        for b in a:
            if b == proper_val:
                x = [list1.index(a), a.index(b)]
                return x
    return None

def trapped_knight_turn(board, position, count, banned_vals, square):
    '''
    Parameters
    ----------
    board : list
        list of lists (nxn matrix of numbers representing centre of spirally enumerated infinite chess board).
    position : list
        position coordinates (index of position).
    count : int
        number of iterations.
    banned_vals : list
        list of forbidden numbers on the chess board.

    Returns
    -------
    new_position : list
        index of position after smallest-valued knight's move.
    board : list
        board as above (might have had layer(s) added).
    '''
    
    for v in banned_vals:
        coords = finds(board, v)
        if coords != None:
            board[coords[0]][coords[1]] = 0
        
    l = len(board)
    
    
    if square:
        func = layer
    
    else:
        func = triangle_layer
        
    vals = []
    nook_vals = []
    for move in possible_moves:
        skip = False
        new_pos = [position[0] + move[0], position[1] + move[1]]
        
        for index in new_pos:
            changed = False
            
            if square:
                if index > l - 1 or index < 0:
                    board = func(board)
                    board = func(board)
                    l = len(board)
                    changed = True
                    break
                
            else:
                if index > l - 1:
                    board = func(board)
                    board = func(board)
                    l = len(board)
                    changed = True
                    break
                elif index < 0:
                    skip = True
        if skip:
            continue
        
        if changed and square:
            position[0] += 2
            position[1] += 2
            new_pos = [position[0] + move[0], position[1] + move[1]]

        new_value = board[new_pos[0]][new_pos[1]]
        
        if new_value != 0:
            vals.append(new_value)
        
        nook_vals.append(new_value)

    if vals == []:
        return board[position[0]][position[1]], 0
    

    board[position[0]][position[1]] = 0
    proper_val = min(vals)
    
    #janky matplotlib stuff
    movement = possible_moves[(nook_vals.index(proper_val))]
    xs.append(movement[0])
    ys.append(movement[1])
    
    new_position = finds(board, proper_val)
    
    return new_position, board

def main(possible_moves, board, position, banned_vals, board_type):
    '''
    Parameters
    ----------
    possible_moves : list
        list of allowed knight's moves.
    board : list
        list of lists (nxn matrix of numbers representing centre of spirally enumerated infinite chess board).
    position : list
        position coordinates (index of position).
    banned_vals : list
        list of forbidden numbers on the chess board.

    Returns
    -------
    int
        value at which the knight becomes trapped.
    '''
    count = 0
    
    while count > -1:
        b_position = position.copy()
        b_board = board.copy()
        position, board = trapped_knight_turn(board, position, count, banned_vals, board_type)
        
        if board == 0:
            return trapped_knight_turn(b_board, b_position, count, banned_vals, board_type)[0]
            break

        if count % 10000 == 0:
            print(count)
            
        count += 1
    return trapped_knight_turn(board, position, count, banned_vals, board_type)

b1 = [[1]]
b2 = [[9, 2, 3], [8, 1, 4], [7, 6, 5]]
banned_vals = [2084, 2720, 3325, 3753, 7776, 5632, 7411, 8562]
banned_vals = [1378, 23016, 4296]
#print(triangle_layer(tb2))



print(main(possible_moves, base, position, banned_vals, True))   

real_xs = []
real_ys = []

for i in range(len(xs)):
    if i == 0:
        real_xs.append(xs[i])
        real_ys.append(ys[i])
    else:
        real_xs.append(real_xs[i-1] + xs[i])
        real_ys.append(real_ys[i-1] + ys[i])
times = np.arange(0, len(real_xs))



###
# Create a set of line segments so that we can color them individually
# This creates the points as a N x 1 x 2 array so that we can stack points
# together easily to get the segments. The segments array for line collection
# needs to be (numlines) x (points per line) x 2 (for x and y)
points = np.array([real_xs, real_ys]).T.reshape(-1, 1, 2)
segments = np.concatenate([points[:-1], points[1:]], axis=1)

fig, ax1 = plt.subplots(1, 1, sharex=True, sharey=True)

# Create a continuous norm to map from data points to colors
norm = plt.Normalize(min(times), max(times))
lc = LineCollection(segments, cmap='viridis', norm=norm)
# Set the values used for colormapping
lc.set_array(times)
lc.set_linewidth(2)
line = ax1.add_collection(lc)
fig.colorbar(line, ax=ax1)

ax1.set_xlim(min(real_xs) - 1, max(real_xs) + 1)
ax1.set_ylim(min(real_ys) - 1, max(real_ys) + 1)
plt.show()
###
