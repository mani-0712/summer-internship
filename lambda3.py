#passing a lambda function as an expression....
def func(f,n):
    print(f(n))
twice = lambda a : 2
func(twice,4)
