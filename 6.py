with open("input.txt","r") as infile, open("output.txt","w") as outfile:
     lines=infile.readlines()
     lines.sort()
     for line in lines:
          outfile.write((line))
          
