#!/usr/bin/env python
fib_values = {0 : 0, 1 : 1}

def fibinaci(n):
    # write the body of your function here
    if n < 0:
        raise Exception('Value must be >= 0')
    if n in fib_values:
        return fib_values[n]
    fib_values[n] = fibinaci(n - 2) + fibinaci(n - 1)
    return fib_values[n]

# run your function through some test cases here
# remember: debugging is half the battle!
# print fibinaci(0)
# print fibinaci(2)
# print fibinaci(4)
# print fibinaci(6)
# print fibinaci(10)

def bottom_up(n):
    """calculate fibonacci from the bottom up. useful for rare calculations"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    prev2 = 0
    prev1 = 1
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
        
    return current

print bottom_up(0)
print bottom_up(2)
print bottom_up(4)
print bottom_up(6)
print bottom_up(10)
