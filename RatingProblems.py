n,k=map(int,input().split())

rates=0
for i in range(k):
    rate=int(input())
    rates+=rate


def maximum(n,k,rates):
    sum=rates
    for i in range(k,n):
        sum+=3
    return sum/n

def minimum(n,k,rates):
    sum=rates
    for i in range(k,n):
        sum+=-3
    return sum/n

print(minimum(n,k,rates),maximum(n,k,rates))
    