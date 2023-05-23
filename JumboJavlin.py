
def length(rods):
    
    total_len=0
    no_rods=len(rods)-1
     
    for rod in rods:
        total_len+=rod
    total_len-=no_rods
    return total_len
    
    


if __name__=='__main__':
    
    no_rods=int(input())
    
    rods=list()
    for i in range(no_rods):
        
        rods.append(int(input()))
    total_length=length(rods)
    
    print(total_length)

        