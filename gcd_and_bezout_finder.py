# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 18:10:29 2022

@author: A Ramsey
"""
import math

def rewrites_pairs(bigger, smaller):
    
    multiplier = math.floor(bigger/smaller)
    remainder = bigger - (multiplier * smaller)
    
    return multiplier, remainder

def gcd_finder(num1, num2):
    '''
    Parameters
    ----------
    num1 : int
        find number.
    num2 : int
        second number.

    Returns
    -------
    gcd : int
        gcd(num1, num2).
    list_of_pairs : list
        list of multipliers and remainders found via the Euclidean algorithm (for use in backsubstitution).
    '''
    bigger = max(num1, num2)
    smaller = min(num1, num2)
    list_of_pairs = []
    real_smaller = smaller
    
    while len(list_of_pairs) == 0 or list_of_pairs[-1] != 0:
        multiplier, remainder = rewrites_pairs(bigger, smaller)
        list_of_pairs.append(multiplier)
        list_of_pairs.append(remainder)
        bigger = smaller
        smaller = remainder
        
    if len(list_of_pairs) < 3:
        gcd = real_smaller
        
    else:
        gcd = list_of_pairs[-3]
        
    return gcd, list_of_pairs

num1 = int(input("number 1: "))
num2 = int(input("number 2: "))
gcd, list_of_pairs = gcd_finder(num1, num2)
print("\n")
print("gcd(%d, %d) = %d \n"%(num1, num2, gcd))

def bezout_finder(num1, num2):
    '''
    Parameters
    ----------
    num1 : int
        first number.
    num2 : int
        second number.

    Returns
    -------
    big_bez : int
        bezout coefficient of larger number.
    small_bez : int
        bezout coefficient of smaller number.
    '''
    gcd, list_of_pairs = gcd_finder(num1, num2)
    
    if len(list_of_pairs) == 2:
        big_bez = 1
        small_bez = (list_of_pairs[0] * -1) + 1
        return big_bez, small_bez
    
    big_bez = 1
    small_bez = list_of_pairs[-4] * -1
    
    for n in range((int(len(list_of_pairs)/2) - 2)):
        big_bez_next = small_bez 
        small_bez_next = big_bez + (small_bez * (list_of_pairs[-6-(2*n)]*-1))
        big_bez = big_bez_next
        small_bez = small_bez_next
        
    return big_bez, small_bez

big_bez, small_bez = bezout_finder(num1, num2)

if gcd == (big_bez * max(num1, num2)) + (small_bez * min(num1, num2)):
    print("%d = %d*%d + %d*%d"%(gcd, big_bez, max(num1, num2), small_bez, min(num1, num2)))

else:
    print("oops! it seems there's been an error! (results don't match)")