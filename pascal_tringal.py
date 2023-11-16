# print(" ",end="")
# print(1)
# print(1,end=" ")
# print(1)

# a=1506
# sum=0
# for i in str(a):
#     sum+=int(i)
# print(sum)



# revers a number.....................
t = int(input())
for i in range(t):
    reverse = 0
    num = int(input())
    while(num):
        remainder = num%10
        reverse =reverse*10+remainder
        num = int(num/10)
    print(reverse)