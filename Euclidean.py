num=[2,3,4,5,6,7,8,9,10]

def even(num):
    for i in range(len(num)):
        if num[i]%2==0:
            print(f'{num[i]} is even')
        else:
            print(f'{num[i]} is odd')
            
even(num)