# Complexity

(Learning from: http://discrete.gr/complexity/)

## Motivation:
'Profilers' are the tools which measures how fast a program runs in milliseconds and can also help us find bottlenecks in our code. 

It is alright as we do not want to measures our programs but the 'ideas' of algorithms. We should not measure implementation of the algorithm because comparing the implementation of an algorithm is not pragmatic. A bad algorithm implemented in the assembly language can run faster than the good algorithm implemented in the high level language like Python, Ruby etc. 

Algorithms are programs that perform just a computation. Complexity analysis is the way to determine how fast a program is when it perform computation. In other words, complexity analysis is the way to determine how fast our algorithm is. Examples of program that just perform computations are:

1. Numeral floating point operations such as addition and subtraction.
2. Searching within a database that fits in RAM for a given value.
3. Determining the path an artificial intelligence character will walk through in a video game so that they only have to walk a short distance within their virtual world. 
4. Running a regular expression pattern to match a string.

Complexity analysis is also a tool which helps to find out how the algorithm will behave when the input grows larger. If our algorithm takes 1 second to run an input size of 1000, then what will happen if we increase the size to double. Will our algorithm runs in the same time, half of the time or runs 4 times slower? It gives us insight about how long our code will run for the largest testcase that are use to test our program's correctness.

## Rules and Info:
1. Rule: Any program that does not have any loops will have f(n) = 1 complexity (unless it uses Recursion) 
2. Rule: Any program that uses single loop will go from 1 to n and will have f(n) = n
3. Given a series of for loops that are sequential, the slowest of them determines the asymptotic behavior of the program. Two nested loops followed by a single loop is asymptotically the same as the nested loops alone, because the nested loops dominate the simple loop.Which means (n^2 + n) is f(n^2)
4. Theta (Θ) represents the time complexity or just complexity.
5. We have special names for common time complexities:
    1. Θ(1): Constant-time algorithm
    2. Θ(n): Linear
    3. Θ(n^2): Quadratic
    4. Θ(log(n)): logarithmic
6. Rule: Programs with a bigger Θ run slower than programs with a smaller Θ.
7. TBC