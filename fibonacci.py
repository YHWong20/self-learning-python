# Fibonacci Number Generator

# To get nth Fibonacci Number
n = int(input("Generate nth Fibonacci Number. What is n? :"))
def fibo(n):
    if n < 0:
        return ValueError("Error: n should be at least 0")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

print(f"The {n}th Fibonacci number is: {fibo(n)}")


# To get range of n Fibonacci numbers
def fibo_rg(n): # While loop, return str
    lst = []
    x = 1
    while x >= 1:
        lst.append(str(fibo(x)))
        x += 1
        if x == n+1:
            break
    return ", ".join(lst)

print(f"Using While Loop, the first {n} Fibonacci numbers are: {fibo_rg(n)}")


def fibo_rg_for(n): # For loop, return list with int
    lst = []
    for i in range(n+1):
        if i == 0:
            continue
        lst.append(fibo(i))
    return lst

print(f"Using For Loop, the first {n} Fibonacci numbers are: {fibo_rg_for(n)}")

    
