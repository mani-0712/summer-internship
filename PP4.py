#swap 2 variables using ^ operators
a=int(input())
b=int(input())
print("before swapping :",a,b)
a=a^b
b=a^b
a=a^b
print("after swapping :",a,b)
