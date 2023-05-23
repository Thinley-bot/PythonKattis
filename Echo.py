line=int(input())

words=[]
for i in range(line):
    inp=input()
    words.append(inp)
    
for i in range(len(words)):
    if i%2==0:
        print(words[i])



    