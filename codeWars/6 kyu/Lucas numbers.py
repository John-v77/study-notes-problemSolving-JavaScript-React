# Lucas numbers are numbers in a sequence defined like this:

# L(0) = 2
# L(1) = 1
# L(n) = L(n-1) + L(n-2)
# Your mission is to complete the function that returns the nth term of this sequence.

# Note: It should work for negative numbers as well; how you do this is you flip the equation around, so for negative numbers: L(n) = L(n+2) - L(n+1)

# Examples
# L(-10) = 123
# L(-5)  = -11
# L(-1)  =  -1
# L(0)   =   2
# L(1)   =   1
# L(5)   =  11
# L(10)  = 123

# Solution

def lucasnum(n):
    a = 2
    b = 1

    flip = n < 0 and n % 2 != 0

    for _ in range(abs(n)):
        a, b = b, a + b
    
    return -a if flip else a