# Write a program to create a function that takes two arguments, name and age, and print their value.
# def na():
    # n=(input("enter name "))
#     a=int(input("enter value "))
#     print(n,a)
# na()

# 0r...........
# def ng(a,b):
#     print(a,b)
# ng("asmita",25)





# Write a program to create function func1() to accept a variable length of 
# arguments and print their value.
# def func1(a,b):
#     print(a,b)
# a=int(input())
# b=int(input())
# func1(a,b)






# Write a program to create function calculation() such that it can accept two 
# variables and calculate addition and subtraction. Also, it must return both 
# addition and subtraction in a single return call.

# def add_sum(a,b):
#     return a+b,a-b
# a=int(input())
# b=int(input())
# result=add_sub(a,b)
# print(result)





# Write a program to create a function show_employee() using the following conditions.
# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

# def show_employee(name, salary=900000):
#     print("name ",name, "salary ",salary)

# show_employee("asmi",200000)
# show_employee("ami")




# Create an outer function that will accept two parameters, a and b
# Create an inner function inside an outer function that will calculate 
# the addition of a and b
# At last, an outer function will add 5 into addition and return it

# def calculation(a,b):
#     def sum():

#         return a+b
    
#     result=sum()

#     print(result)

#     return result+5

# add_5=calculation(3,4)

# print(add_5)






# Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

# A recursive function is a function that calls itself again and again.

# def calcution():
#     i=1
#     sum=0
#     while(i<=5):
#         sum+=i
#         i+=1
#     return sum
# print(calcution())




# Exercise 7: Assign a different name to function and call it through the new name
# Below is the function display_student(name, age). Assign a new name show_tudent(name, age) 
# to it and call it using the new name.

# def display_student(name,age):
#     print(name,age)


# # # call function using oringel name
# # name=input()
# # age=int(input())
# # display_student(name,age)

# show_student=display_student

# name=input()
# age=int(input())
# show_student(name,age)



# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
# def list():
#     array=[]
#     for i in range(4,31):
#         if i%2==0:
#             array.append(i)
#     print(array)
# list()



# Exercise 9: Find the largest item from a given list
def largest():
    x = [4, 6, 8, 24, 12, 2]
    s=len(x)
    max=x[0]
    for i in range(s):
        if max<x[i]:
            max=x[i]
    return max
print(largest())






