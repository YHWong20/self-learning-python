n = int(input("Number of Fibonacci Numbers: "))
if n < 1:
  raise ValueError("Number must be at least 0") # n has to be greater than 0

def fib(n): # recursion
  if n == 0:
    return 0
  elif n == 1:
    return 1
  return fib(n - 1) + fib(n - 2)

def fib_seq(n): # while loop
  lst = []
  x = 1
  while x >= 0:
    lst.append(fib(x))
    x += 1
    if x == n+1:
      break
  return lst

def fib_seq_two(n): # for loop
  lst = []
  for i in range(n+1):
    lst.append(fib(i))
  return lst[1:]
    

print(f"List of the first {n} Fibonacci Numbers: {fib_seq(n)}")
print(fib_seq_two(n))

