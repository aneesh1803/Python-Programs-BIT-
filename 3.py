import math

n=int(input("Enter the number of elements: "))

numbers=[]

for i in range(0,n):
     print("Enter number",i+1,": ",end='')
     elements=float(input())
     numbers.append(elements)

mean=sum(numbers)/n
variance= sum((x-mean)**2 for x in numbers)
std_dev=math.sqrt(variance)

print("Mean:",mean)
print("Variance",variance)
print("Standard Deviation:",std_dev)
