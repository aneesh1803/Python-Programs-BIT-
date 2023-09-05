
class Student:
     def __init__(self,name,usn):
          self.name=name
          self.usn=usn
          self.marks=[0,0,0]
          self.total=0

     def getMarks(self):
          for i in range(3):
               self.marks[i]= int(input(f"Enter marks for subject {i+1}: "))
          self.total= sum(self.marks)

     def display(self):
          print("Scorecard")
          print("Name: ",self.name)
          print("USN: ",self.usn)
          print("Marks:")
          for i in range(3):
               print(f"Subject {i+1}: {self.marks[i]}")

          print("Total: ",self.total)
          print("Percentage: ",(self.total/3),"%")

name=input("Enter Name: ")
usn=input("Enter USN: ")
s=Student(name,usn)
s.getMarks()
s.display()
