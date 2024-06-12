#swap 3 variables using + and - operators
a=int(input())
b=int(input())
c=int(input())
print("before swapping :",a,b,c)
a=a+b+c
b=a-(b+c)
c=a-(b+c)
a=a-(b+c)
print("after swapping :",a,b,c)
