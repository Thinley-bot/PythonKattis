class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        n1,n2=0,1
        count=0
        
        if n<=0:
            return "enter positive number"
        
        while count<=n:
                nth=n1+n2
                n1,n2=n2,nth
                count+=1
        return n1
                
s1=Solution()

n=int(input())

print(s1.climbStairs(n))
    
            
            
   
            
            
            
            