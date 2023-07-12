#Read Name, usn, marks or three subjects
#display student details, total marks, percentage with suitable message

name=input("Enter the Name of the student: ")
usn=input("Enter the USN: ")
m1=float(input("Enter the marks of subject 1: "))
m2=float(input("Enter the marks of subject 2: "))
m3=float(input("Enter the marks of subject 3: "))

sum=m1+m2+m3
percentage=(sum/3)

print("\nStudent Details")
print("Name=",name,"\nUSN=",usn,)
print("Marks in subject 1:", m1)
print("Marks in subject 2:", m2)
print("Marks in subject 3:", m3)
print("Total marks obtained:",sum)
print("Percetnage obtained:",percentage,"%")

if percentage >= 60:
      
     print("Congratulations, you have passed with first division!")
elif percentage >= 45:
     print("Congratulations, you have passed with second division!")
elif percentage >= 35:
     print("Congratulations, you have passed with third division!")
else:
     print("Sorry, you have failed the exam.")








