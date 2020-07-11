#recurrsion gcd
def gcd(x,y):
    if y%x==0:
        return x
    else:
        return gcd(y%x,x)
x,y=map(int,input().split())
print(gcd(x,y))
