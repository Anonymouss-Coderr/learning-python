

#float type
#used for decimal numbers

x=float(input("Enter the 1st number: ")) 
y=float(input("Enter the 2nd number"))

z=x+y
print(z)


#Boolean variables can be used to represent the presence or absence of a student. 
# In this case, we can use a boolean variable called 'student_present' to indicate whether the student is present or not.
#  If the value of 'student_present' is True, it means the student is present, and if it is False,
#  it means the student is not present.

student_present = False

print(f"Is the student present? {student_present}") #here f is used to format the string and include the value of the boolean variable 'student_present' in the output.

if student_present:
    print("The student is present.")
else:
    print("The student is not present.")