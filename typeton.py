stringvar: str = "thisisastring"

print(stringvar)
print(type(stringvar))

stringvar = 1

print(stringvar)
print(type(stringvar))

intvar: int = 2

print(intvar)
print(type(intvar))

intvar: int = "string 3"

print(intvar)
print(type(intvar))


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1)+fib(n-2)
    
print(fib(10))