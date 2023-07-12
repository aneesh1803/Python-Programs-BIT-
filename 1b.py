#Read Name and Year of birth. Display is the person is senior citizen or not

name=input("Enter name: ")
year=int(input("Enter the year of birth: "))

currentyear=2023

age=currentyear-year

is_senior=(age>=60)

print("Name:",name)
print("Age:",age)

if is_senior:
     print("This person is senior citizen.")
else:
     print("This person is not senior citizen")
