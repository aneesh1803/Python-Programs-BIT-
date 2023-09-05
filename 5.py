#10 most frequently appearing words in a text file

with open("sample.txt","r") as file:     #replcae your txt file here
     text=file.read()

text=text.lower()

for p in [",",".","?","!",":",";"]:
     text=text.replace(p," ")

words=text.split()
freq={}

for word in words:
     if word in freq:
          freq[word]+=1
     else:
          freq[word]=1

sortedfreq=sorted(freq.items(),key=lambda x: x[1], reverse=True)

print("The 10 most frequently appearing words are: ")
for word,fr in sortedfreq[:10]:
     print(word,":",str(fr))
