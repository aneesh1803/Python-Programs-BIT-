class Complex:
     def __init__(self,real,imag):
          self.real=real
          self.imag=imag

     def __add__(self,other):
          return Complex(self.real+other.real, self.imag+other.imag)

def add_complex(c1,c2):
     return c1+c2

n= int(input("Enter the number of complex numbers: "))
numbers=[]

for i in range(n):
     print(f"Enter the complex number {i+1}: ")
     real=float(input("Real part: "))
     imag=float(input("imaginary part:"))
     numbers.append(Complex(real,imag))

result=numbers[0]

for i in range(1,n):
     result = add_complex(result,numbers[i])

print(f"The sum of the complex numbers is: {result.real} + {result.imag}i")
