'''
When you run a function:
1. Memory is allocated for the function
2. Variables created / used in a function are "local" to the function
    they get their values in the function and don't affect variables
    using the same name in the main program or other functions
When a function returns:
1. memory for the function, including local variables is freed and goes away


'''


name= "James Bond"
sloc = name.find(" ")
first = name[0:sloc]
last = name[sloc+1:]
print(last + ", " + name)

def myfirstfunc():
    print("I'm in the function")
    print("I'm still in the function")
    
def f():
    x = 30
    print(x)


x = 20
print(x)
f()
