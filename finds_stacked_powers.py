# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 16:46:33 2022

@author: A Ramsey
"""

def finds_stacked_powers(a, r, n):
    '''
    Parameters
    ----------
    a : int
        base number.
    r : int
        power of 2.
    n : int
        modulus.

    Returns
    -------
    to_sub : int
        a^(2^r) mod n.
    '''
    to_sub = a % n
    for R in range(1, r+1):
        to_sub = (to_sub * to_sub) % n
    return to_sub

#print(finds_stacked_powers(56, 93, 63))