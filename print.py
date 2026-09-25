
#the print function will have the following parameters:
#sep: This parameter specifies the string that will be used to separate the objects being printed. By default, it is set to a space character (' ').
#end: This parameter specifies the string that will be printed at the end of the output.



#print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

name = input("Enter your name: ")
print("Hello ," )
print(name)


print("Hello, ", end="")
print(name)

print("Hello, ", end="?!?")
print(name)

print("Hello, ",name, sep="***") 
