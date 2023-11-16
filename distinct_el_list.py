# 8. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def list(n):
    l=[]
    for i in range(n):
        a=int(input())
        l.append(a)
    return l
n=int(input("lenth og list"))
x=list(n)

def new_list():
    l1=[]
    for i in range(n):
        c=0
        for j in range(i+1,n):
            if x[i] == x[j]:
                c=1
                j+=n
        if c==1:
           pass
        else:
            l1.append(x[i])
    return l1
print(new_list())
