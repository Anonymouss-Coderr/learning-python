
# WE CAN USE f strings to format strings in Python. The f before the string allows us to include 

name=input("Enter your name: ")
print(f"Hello, {name}")   # variables directly within the string using curly braces {}. In this case, the variable 'name' is included in the output string.


name=name.strip()  # strip() -- Remove whitespace from str, str like "      abc      " will be converted to "abc"
print(f"Hello, {name}") 

name = name.capitalize()  # capitalize() -- Convert the first character to upper case, dosent change the rest of the characters in the string. 
print(f"Hello, {name}")   #if name is abc def, it will be converted to Abc def

name = name.title() # to convert the first character of each word to upper case, we can use title() method.
print(f"Hello, {name}")  #if name is abc def, it will be converted to Abc Def

name=name.strip().capitalize()  # we can also chain the methods together to achieve the same result in a single line of code.
print(f"Hello, {name}")

#we can also use these put strip() and title() methods together to "" name=input("Enter your name: ") ""
name=input("Enter your name: ").strip().title()  # we can also chain the methods together to achieve the same result in a single line of code.
print(f"Hello, {name}")





#to split the name into first name and last name, we can use the split() method.
#The split() method splits a string into a list of substrings based on a specified delimiter.
#By default, it splits the string at whitespace characters (spaces, tabs, newlines).


name = input("Enter your name: ")
first , last = name.split(" ") # here spcae is used as a delimiter to split the name into first name and last name.
print(f"Hello, {first}") 