# 10. Write a Python program to print the even numbers from a given list.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
def list(n):
    l=[]
    for i in range(n):
        a=int(input())
        l.append(a)
    return l
n=int(input())
x=list(n)
# n=8
# x=[1,2,3,4,5,6,7,8]
def even():
    for j in range(n):
        if x[j]%2==0: 
            print(x[j],end=" ")
even()
                                                                                                                