# mathematical-programs

Maths-related programs (written for fun):

1. abelian_groups: finds all abelian groups of a given order, and finds the abelian groups without elements of given orders. Written in SageMath. 

2. brot: plots the mandelbrot set using matplotlib: the coordinates for several interesting regions are given at various magnifications.

3. cubic_curves: equips a smooth cubic curve with its abelian group structure, and finds the sum of any two points on it. Written in SageMath.

4. gcd_and_bezout_finder: uses the Euclidean algorithm to find the gcd and bezout coefficients of any two integers.

5. knights_tour: finds and plots a knight's tour (a Hamiltonian path of a knight on a chessboard).

6. polys_over_Fp: collection of functions investigating polynomials over the field $\mathbb{F}_p$. In particular, calculating the number of reducible (or irreducible) polynomials of degree $k$ over $\mathbb{F}_p$ for a given natural number $k$ and prime $p$. Another function ("norm") displays the proportion of reducible polynomials of degree $k$ as $p$ tends to infinity. 

7. primes_and_all_they_entail: collection of functions to do with prime numbers, including a generator of prime numbers, a function which checks whether a number is prime (using the Miller-Rabin primality test) and a function which tries to figure out which are the least reliable 'witness numbers' when using this test.

8. trapped_knight_better: simulates the 'trapped knight' problem - if a knight is placed on an infinite chess board, enumerated spiralling outwards from the starting position, and moves to the lowest number possible, on which square will it get trapped (a graph is also plotted to visualise this)? What is the sequence of numbers corresponding to the squares it gets trapped on (if each previous one is removed)? And what if we start at a corner? Inspired by the Numberphile video: https://youtu.be/RGQe8waGJ4w
