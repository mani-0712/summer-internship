#passing a lambda function as an expression....
def func(f,n):
    print(f(n))
twice = lambda a : a*2
thrice = lambda a: a*3
func(twice,4)
func(thrice,5)
