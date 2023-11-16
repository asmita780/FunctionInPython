# 5. Write a Python function to calculate the factorial of a number 
# (a non-negative integer). The function accepts the number as an argument.

def factorial(a):
    i=a
    f=1
    while i>0:
        f*=i
        i-=1
    print(f)
# a=int(input())
factorial(6)
