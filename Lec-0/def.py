

def hello(to):          #here hello is a function which takes one argument "to"
    print("Hello,",to)

name = input("Enter your name: ")
hello(name)             #here we are calling the function hello and passing the value of name as an argument to it.


def helloo(to="World"): #here helloo is a function which takes one argument "to" and has a default value of "World", when no argument is passed to it.
    print("Hello,", to)

name = input("Enter your name: ")
helloo()                #here we are calling the function helloo without passing any argument, so it will use the default value "World".                    
helloo(name)            #here we are calling the function helloo and passing the value of name as an argument to it.



 #using return statement in function

def main():
    x = int(input("Enter a number: "))
    print("The square of", x, "is", square(x))  #here we are calling the function square and passing the value of x as an argument to it.


def square(n):
    return n ** 2 # here we are returning the value of n raised to the power of 2 from the function square.

main() #here we are calling the function main to execute the code inside it.

#we can only use an variable inside a function if it is defined inside the function or passed as an argument to the function. 
#If we try to use a variable that is not defined inside the function or passed as an argument, we will get an error.