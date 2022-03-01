from math import sqrt, ceil

# prime number checker
def prime_checker_for(n):
    if n <= 0:
        return f"{n} is not a prime number"
    elif n == 1 or n == 2:
        return f"{n} is a prime number"
    else:
        for i in range(2, int(ceil(sqrt(n))) + 1):
            if n % i == 0:
                return f"{n} is not a prime number"
    return f"{n} is a prime number"

# print(prime_checker_for(17)) # True

def prime_checker_while(n):
    if n <= 0:
        return f"{n} is not a prime number"
    elif n == 1 or n == 2:
        return f"{n} is a prime number"
    count = 2
    while count <= int(sqrt(n)):
        if n % count == 0:
            return f"{n} is not a prime number"
        count += 1
    return f"{n} is a prime number"

# print(prime_checker_while(8)) # False


# fibonacci number checker
# assumes positive fibonacci numbers only
def fib_check(n):
    if n == 0:
        return f"{n} is a Fibonacci number"
    fib_x_minus_one, fib_x = 0, 1
    while n >= fib_x:
        if n == fib_x:
            return f"{n} is a Fibonacci number"
        fib_x_minus_one, fib_x = fib_x, fib_x_minus_one + fib_x
    return f"{n} is not a Fibonacci number"

# print(fib_check(160500643816367088)) # True
# print(fib_check(7)) # False


# triangle number and triangle number sum checker
def is_triangle(n):
    nth_triangle, counter = 0, 0
    while n >= nth_triangle:
        if n == nth_triangle:
            return f"{n} is a triangle number"
        nth_triangle += counter
        counter += 1
    return f"{n} is not a triangle number"

# print(is_triangle(3)) # True
# print(is_triangle(27)) # False

def is_triangle_sum(n): # sum of triangle numbers checker
    nth_triangle, nth_sum, counter = 0, 0, 0
    while n >= nth_sum:
        if n == nth_sum:
            return f"{n} is a triangle sum"
        nth_sum += nth_triangle
        nth_triangle += counter
        counter += 1
    return f"{n} is not a triangle sum"

# print(is_triangle_sum(119)) # False
# print(is_triangle_sum(120)) # True
        

# square number checker
def sq_check(n):
    counter = 1
    while n >= counter ** 2:
        if n == counter ** 2:
            return f"{n} is a square number"
        counter += 1
    return f"{n} is not a square number"

# print(sq_check(26)) # False
# print(sq_check(121)) # True

