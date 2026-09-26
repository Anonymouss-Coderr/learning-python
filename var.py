

#float type
#used for decimal numbers
a=input("Do u want to execute the float type code? (y/n): ")
if a == "y":
    x=float(input("Enter the 1st number: ")) 
    y=float(input("Enter the 2nd number: "))
    z=x+y
    print(z)

#to round of the float num we can use round() function. The round() function takes two arguments:
#the number to be rounded and the number of decimal places to round to.

    z=round(x+y)
    print(z)   # this will round off the float number to the nearest integer.

# if we want to add comma as a separator for thousands, we can use this syntax
# print(f"{z:,}")  # this will add comma as a separator for thousands.

    print(f"{z:,}")



#Boolean variables can be used to represent the presence or absence of a student. 
# In this case, we can use a boolean variable called 'student_present' to indicate whether the student is present or not.
#  If the value of 'student_present' is True, it means the student is present, and if it is False,
#  it means the student is not present.
elif a == "n":
    b=input("Do u want to execute the boolean type code? (y/n): ")
    if b == "y":
        student_present = True
        print(f"Is the student present? {student_present}") #here f is used to format the string and include the value of the boolean variable 'student_present' in the output.

        if student_present:
            print("The student is present.")
        else:
            print("The student is not present.")
    else:
        print(" ")

else:
    print (" ")

    
