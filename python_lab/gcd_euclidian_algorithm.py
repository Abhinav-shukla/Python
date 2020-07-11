#euclidian algorithm
def gcd(a,b):
    while(b%a!=0):
        temp=b
        b=a
        a=temp%a
    print(a)
x,y=map(int,input().split())
gcd(x,y)
