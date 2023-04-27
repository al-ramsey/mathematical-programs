# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 16:28:18 2023

@author: A Ramsey
"""
#import sympy as sym
from sympy import symbols
from sympy import factorial
from sympy import simplify
from sympy import Poly
import time

p = symbols('p')

def choose(p, i): 
    return factorial(p)/(factorial(i)*factorial(p-i))

def xi(p, k):
    '''
    Parameters
    ----------
    p : symbol
        variable representing a prime number p.
    k : int
        degree of polynomials considered in F_p[X].

    Returns
    -------
    x : sympy polynomial
        polynomial in p representing the number of reducible polynomials of order k in F_p[X].
    '''
    # summing over possible numbers of linear factors
    s1 = 0 
    for i in range(k+1):
        s2 = 0
        if i == 0: # no linear factors
            s2 = 1 # p choose 0 = 1
        else:
            for j in range(1, i+1):
                s2 += choose(p, j) # accounts for j distinct roots
        s3 = 0
        
        if finds_partitions(k-i) == [[0]]:
            s3 = 1 # convention: there is one partition of 0 elements
        else:
            for j in finds_partitions(k-i): # summing over possible combinations of irreducible polynomials of degree k-i
                if i == 0 and len(j) == 1: # discount partition [k] with (0 linear factors) since would not be reducible
                    continue
                else:
                    p1 = 1
                    for nj in j:
                        p1 *= ((p**nj) - xi(p, nj)) # number of irreducible polynomials of order nj
                    s3 += p1
                
        s1 += s2*s3
        
    x = s1
    return x

def efficient_xi(p, k):
    '''
    Parameters
    ----------
    p : symbol
        variable representing a prime number p.
    k : int
        degree of polynomials considered in F_p[X].

    Returns
    -------
    x : sympy polynomial
        polynomial in p representing the number of reducible polynomials of order k in F_p[X].
    '''
    #more efficient than xi for n > 5
    
    # summing over possible numbers of linear factors
    xis = [xi(p, i) for i in range(1, k)]
    s1 = 0
    for i in range(k+1):
        s2 = 0
        if i == 0: # no linear factors
            s2 = 1  # p choose 0 = 1
        else:
            for j in range(1, i+1):
                s2 += choose(p, j) # accounts for j distinct roots
        s3 = 0
        
        if finds_partitions(k-i) == [[0]]:
            s3 = 1 # convention: there is one partition of 0 elements
        else:
            for j in finds_partitions(k-i): # summing over possible combinations of irreducible polynomials of degree k-i
                if i == 0 and len(j) == 1: # discount partition [k] with (0 linear factors) since would not be reducible
                    continue
                else:
                    p1 = 1
                    for nj in j:
                        p1 *= ((p**nj) - xis[nj - 1]) # number of irreducible polynomials of order nj
                    s3 += p1
                
        s1 += s2*s3
        
    x = s1
    return x

def norm(p, k):
    '''
    Parameters
    ----------
    p : symbol
        variable representing a prime number p.
    k : int
        degree of polynomials considered in F_p[X].

    Returns
    -------
    sympy polynomial
        leading coefficient of xi(p, k) (equiv. limit of xi(p, k)/(p^k) as p -> oo.
    '''
    return Poly(simplify(xi(p, k))).coeffs()[0]

def efficient_norm(p, k):
    '''
    Parameters
    ----------
    p : symbol
        variable representing a prime number p.
    k : int
        degree of polynomials considered in F_p[X].

    Returns
    -------
    sympy polynomial
        leading coefficient of xi(p, k) (equiv. limit of xi(p, k)/(p^k) as p -> oo.
    '''
    #more efficient than norm for n > 5
    return Poly(simplify(efficient_xi(p, k))).coeffs()[0] 

def finds_partitions(n): 
    '''
    Parameters
    ----------
    n : int
        number to be partitioned.

    Returns
    -------
    partitions : list of lists
        list of partitions of n.
    '''
    partitions = [[n]]

    while len(partitions[-1]) < n: # last partition as all 1's
        
        count = -1
        for el in reversed(partitions[-1]):
            if el == 1:
                count -= 1
                continue
            else:
                new_el = el - 1
                break
        
        new_partition = partitions[-1][:count]
        new_partition.append(new_el)
        while sum(new_partition) < n:
            if n - sum(new_partition) >= new_el:
                new_partition.append(new_el)
            else:
                new_partition.append(n - sum(new_partition))
        
        partitions.append(new_partition)
        
    return partitions

def irreducible(prime, k):
    '''
    Parameters
    ----------
    prime : int
        prime number.
    k : int
        degree of polynomials.

    Returns
    -------
    n : int
        number of irreducible polynomials of degree k in F_p[X].
    '''
    n = prime**k - xi(p, k).subs(p, prime)
    return n

## tests below ##

#print(simplify(xi(p, 4)))
#print(finds_partitions(3))
#print(norm(p, 5))
    
'''
for j in range(1, 10):
    #print(simplify(xi(p, j)))
    t0 = time.time()
    print(efficient_norm(p, j))
    t1 = time.time()
    print(t1-t0)
    t2 = time.time()
    print(norm(p, j))
    t3 = time.time()
    print(t3-t2)
    print("\n")
'''
'''
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
deg = 2

for prime in primes:
    print(prime**deg - xi(p, deg).subs(p, prime))
'''