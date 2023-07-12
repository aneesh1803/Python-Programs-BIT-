#Fibonacci Series

n=int(input("Enter the length of the Fibonacci sequence: "))

fibonacci=[0,1]

for i in range(2,n):
     next=fibonacci[i-1]+fibonacci[i-2]
     fibonacci.append(next)

print("The Fibonacci Sequence of length",n,"is: ")
for i in fibonacci:
     print(i,end=" ")
