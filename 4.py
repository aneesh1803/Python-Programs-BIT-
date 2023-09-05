#Read multi digit number from the console
#develop a program to print frequency of each digit

number=(input("Enter multi-digit number: "))
frequency={}

for digit in number:
     if digit in frequency:
          frequency[digit]+=1
     else:
          frequency[digit]=1

print("Digit Frequencies: ")
for i in frequency:
     print(i,":",frequency[i])



