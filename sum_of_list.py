# 2. Write a Python function to sum all the numbers in a list.
# Sample List : (8, 2, 3, 0, 7)
# Expected Output : 20 

# def creat_list(n):
#     list=[]
#     for i in range(n):
#         a=int(input())
#         list.append(a)
#     return list
# n=int(input())
# x=creat_list(n)

# def sum():
#     sum=0
#     for i in range(n):
#         sum+=x[i]
#     return sum
# print(sum())

# 2nd mathode...................................
n=int(input())
def creat():
    list=[]
    for i in range(n):
        a=int(input())
        list.append(a)
    sum=0
    for j in range(n):
        sum+=list[j]
    print(sum)
creat()