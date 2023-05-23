input_string = input()

for i in range(1, len(input_string)): 
    if input_string[i - 1] == input_string[i] and input_string[i] == 's':
        print('hiss')
        break
else:
    print('no hiss')