

def hello(to):          #here hello is a function which takes one argument "to"
    print("Hello,",to)

name = input("Enter your name: ")
hello(name)             #here we are calling the function hello and passing the value of name as an argument to it.


def helloo(to="World"): #here helloo is a function which takes one argument "to" and has a default value of "World", when no argument is passed to it.
    print("Hello,", to)

name = input("Enter your name: ")
helloo()                #here we are calling the function helloo without passing any argument, so it will use the default value "World".                    
helloo(name)            #here we are calling the function helloo and passing the value of name as an argument to it.