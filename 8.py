'''Write a function named DivExp which takes two parameters a,b and returns a
a value c (c=a/b). Write a suitable assertion for a>0 in function DivExp and raise
exception for when b=0. Develop a suitable program'''


def DivExp(a,b):
     assert a>0, "a Must be greater than 0"
     if b==0:
          raise Exception("b cannot be 0")
     c=a/b
     return c

a= float(input("Enter the value for a:"))
b= float(input("Enter the value for b:"))


try:
     result=DivExp(a,b)
     print(f"{a}/{b}={result}")

except AssertionError as e:
     print(f"Assertion error: {e}")

except Exception as e:
     print(f"Exception: {e}")
