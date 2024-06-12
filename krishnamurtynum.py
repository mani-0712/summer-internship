#Program to check the given number is Krishnamurthy`s number/Strong number or not.....
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp !=0:
   r = temp % 10
   r1=1
   while r!=0:
       r1=r1*r
       r-=1
   sum += r1
   temp //= 10
print(sum)   
if num == sum:
   print(num,"is an Srtong number")
else:
   print(num,"is not an Strong number")
