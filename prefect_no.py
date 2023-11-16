# 11. Write a Python function to check whether a number is "Perfect" or not.
def prefect(n) :
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum+=i
    if sum/2==n:
        print("prefect")
    else:
        print("not prefect")
n=int(input())
prefect(n)


# def prefect(n) :
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             sum+=i
#     if sum==n:
#         print("prefect")
#     else:
#         print("not prefect")
# n=int(input())
# prefect(n)