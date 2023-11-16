# 4. Write a Python program to reverse a string.
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
def creat_string():
    a=input()
    b=""
    i=len(a)-1
    while i>=0:
        b+=a[i]
        i-=1
    return b
print(creat_string())
