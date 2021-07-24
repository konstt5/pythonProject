def saystr(str):
    print(str)

saystr('1552')

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

#n = int(input())
n = 3
print(f"{n} factorial is {factorial(n)}")

a = None
print(a)