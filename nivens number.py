#program to check the given number is Niven`s number or not....
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp !=0:
   r = temp % 10
   sum += r
   temp //= 10
if num % sum==0:
   print(num,"is an Niven`s number")
else:
   print(num,"is not an Niven`s number")
