line=input()
index=line.find('a')

for i in range(index,len(line)):
    letter=line[i]
    print(letter,end="")

