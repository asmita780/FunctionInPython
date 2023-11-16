# <!-- 1. Write a Python function to find the maximum of three numbers.  -->
def maximum(a,b,c):
    if a<b:
        max=b
    else:
        max=a
    if max<c:
        max=c
    else:
        max=max
    return max
a=int(input())
b=int(input())
c=int(input())
print(maximum(a,b,c))