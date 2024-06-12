#program to check the given number is an Automorphic or not....
num = int(input("Enter a number: "))
num_of_digits = len(str(num))
a=num**2
last_digit = a % pow(10,num_of_digits)
if last_digit == num:
    print("automorphic")
else:
    print("non-automorphic")


    
            
            
