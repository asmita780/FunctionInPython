# 3. Write a Python function to multiply all the numbers in a list.
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336 

n=int(input())
def multiplytion():

    list=[]

    for i in range(n):
        a=int(input())
        list.append(a)

    product=1

    for j  in range(n):
        product*=list[j]
    print(product)

multiplytion()
