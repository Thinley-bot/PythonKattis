# dict={
#     1:"Tashi Wangchuk",
#     2:"Tashi Namgay",
#     3:"Pema Wangmo"
# }

# for key,value in dict.items():
#     if key==1:
#         print(f"This is {value}")
#     else:
#         print("This is nobady")

#Build one simple calculator

from audioop import add


def addition(x,y):
    return(x+y)

def div(x,y):
    while y!=0:
        q=x/y
    return q

def sub(x,y):
    return(x-y)

def mul(x,y):
    return(x*y)

x=int(input("Enter the first num:"))
y=int(input("Enter the second num: "))
acts=input("enter the act:")

if acts=="add":
    print(add(x,y))
elif acts=="div":
    print(div(x,y))
elif acts=="mul":
    print(mul(x,y))
elif acts=="sub":
    print(sub(x,y))

        
        
    
        