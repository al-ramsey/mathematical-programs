# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 14:57:15 2022

@author: A Ramsey
"""

import math

def finds_stacked_powers_of_2(a, r, n):
    '''
    Parameters
    ----------
    a : int
        number you are raising to power of 2^r
    r : int
        number you are raising 2 to the power of
    n : int
        modulo n

    Returns
    -------
    to_sub : int
        a^(2^r) mod n
    
    Status
    -------
    works
    '''
    to_sub = a % n
    for R in range(1, r+1):
        to_sub = (to_sub * to_sub) % n
    return to_sub

def finds_powers_general(b, d, n):
    '''
    Parameters
    ----------
    b : int
        number you are raising to dth power
    d : int
        number you are raising b to the power of
    n : int
        modulo n

    Returns
    -------
    int
        b^d mod n
    
    Status
    -------
    works
    '''
    bin_d = str(bin(int(d)))
    list_of_chars = []
    char_count = 0
    
    for char in bin_d:
        if char_count > 1:
            list_of_chars.append(int(char))
        char_count += 1
        
    list_of_chars.reverse()
    new_list = []
    
    for x in range(len(list_of_chars)):
        powers = list_of_chars[x]*(2**x)
        new_list.append(powers)
        
    mod_mul = 1
    new_count = 0
    
    for power in new_list:
        if power == 0:
            new_count +=1 
            continue
        mod = finds_stacked_powers_of_2(b, new_count, n)
        mod_mul*=mod
        new_count += 1
        
    return mod_mul % n


def prime_list_generator(up_to_n):
    #!! note: this function doesn't work !! (the status lies!!!!!)
    '''
    Parameters
    ----------
    up_to_n : int
        what number you want the list of primes to go up to

    Returns
    -------
    prime_list : list
        list of primes up to and including up_to_n
    
    Status 
    -------
    works
    '''
    prime_list = [2, 3]
    witnesses = [2, 3]
    
    for n in range(4, up_to_n +1):
        if n % 2 == 0:
            continue
        
        m = 0
        
        for x in range(1, int((math.log(n))/(math.log(2)))+1):
            if (n-1) % (2**x) != 0:
                m = x - 1
                break
            else:
                continue
            
        d = (n-1)/(2**m)
        witness_count = 0
        
        for a in witnesses:
            if a**d % n == 1 or a**d % n == (n-1):
                witness_count += 1
                
            elif d > 1:
                for r in range(m):
                    if a**((2**r)*d) % n == 1 or a**((2**r)*d) % n == (n-1):
                        witness_count += 1
                        break
        
        if witness_count == 2:
            prime_list.append(n)
            
    return prime_list

def finds_s(n):
    '''
    Parameters
    ----------
    n : int
        prime we're using

    Returns
    -------
    int
        s such that n = 2**s * d + 1
        
    Status
    -------
    works
    '''
    for s in range(2, n + 1):
                if (n - 1) % (2**s) == 0:
                    continue
                else:
                    return (s - 1)
                
def finds_liars(up_to_a, up_to_n):
    '''
    Parameters
    ----------
    up_to_a : int
        highest witness number you want to check
    up_to_n : int
        highest potential prime number you want to check a against

    Returns
    -------
    int
        number which has "lied" the most about a non-prime being prime
        
    int
        false positive rate for biggest liar
        
    Status
    -------
    unk
    '''
    liar_count_list = []
    
    for a in range(2, up_to_a + 1): # a = witness, a>=2
        liar_count = 0
        start = max(a, 3)
        
        if start % 2 == 0:
            start += 1
            
        n_count = 0
        #next lines of code was initially:
        #for n in range(start, up_to_n + a - 1, 2):
        
        for n in range(start, up_to_n + 1, 2): # looping through potential primes (only odds)
            n_count += 1
            if n in prime_list_generator(up_to_n):
                prime = True # n is prime
            else:
                prime = False
                
            s = finds_s(n)
            d = (n-1)/(2**s)
            
            for r in reversed(range(s+1)): # going backwards through sequence
            #list will be all 1s, or the first non-1 will be a -1
                b = finds_stacked_powers_of_2(a, r, n)
                
                if finds_powers_general(b, d, n) == 1:
                    continue
                elif finds_powers_general(b, d, n) == n-1:
                    a_says_prime = True
                    break
                else:
                    a_says_prime = False
                    break
                
            if prime != a_says_prime:
                liar_count += 1
                
        proportion = liar_count/n_count
        liar_count_list.append(proportion)
        
    return (liar_count_list.index(max(liar_count_list)) + 2), max(liar_count_list)

#print(finds_liars(100, 300))

def better_prime_czecher(p):
    '''
    Parameters
    ----------
    p : int
        number you're checking to see if it's prime

    Returns
    -------
    str
        y/n
    
    Status
    -------
    works :)
    '''
    if p == 2 or p == 3:
        return "Yes!"
    elif p % 2 == 0:
        return "No :("
    if p == 1:
        return "No :("
    
    witnesses = [2, 3]
    witness_count = 0
    
    for a in witnesses:
        bad_count = 0
        
        s = finds_s(p)
        d = (p-1)/(2**s)
        
        for r in reversed(range(s+1)): 
            b = finds_stacked_powers_of_2(a, r, p)
            
            if finds_powers_general(b, d, p) == 1:
                continue
            elif finds_powers_general(b, d, p) == p-1:
                witness_count += 1
                break
            else:
                bad_count += 1
                break
            
    if witness_count == 2:
        return "Yes!"
    elif bad_count == 0:
        return "Yes!"
    else:
        return "No :("
    
#print(better_prime_czecher(7))

for n in range(1, 100):
    if better_prime_czecher(n) == "Yes!":
        print(n)

def non_shit_prime_generator(up_to_n):
    our_list = []
    
    for n in range(1, up_to_n):
        if better_prime_czecher(n) == "Yes!":
            our_list.append(n)
            
    return our_list

#print(non_shit_prime_generator(100))