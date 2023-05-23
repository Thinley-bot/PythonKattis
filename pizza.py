from math import sqrt

no_order=int(input())


for i in range(no_order):
    n,s=map(int,input().split())
    height=sqrt(3) * (s/2)
    print(height)

    length= n*s
    # for k in range(n):
    #     length+=s
    print(length)
    min_area=round(height*length,3)
    print(f"Order #{i+1}:",min_area)

    
    
    
