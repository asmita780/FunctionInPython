# 7. Write a Python function that accepts a string and counts the number of upper and lower case letters.
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

def count():
    a=input()
    c=0
    c1=0
    for i in range(len(a)):
        if "A"<a[i]<="Z":
            c+=1
        else:
            if "a" < a[i] <= "z":
                c1+=1
    print("upper",c, "lower",c1)
count()