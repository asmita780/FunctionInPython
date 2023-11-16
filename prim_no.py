# 9. Write a Python function that takes a number as a parameter and 
# checks whether the number is prime or not. 
def prime_no(a):
    c=0
    for i in range(1,a+1):
        if a%i==0:
            c+=1
    if c==2:
        print("prime")
    else:
        print("not prime")
a=int(input())
prime_no(a)
