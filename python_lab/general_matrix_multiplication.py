m,n=map(int,input("Enter matrix 1 size:").split())
p,q=map(int,input("Enter matrix 2 size:").split())
print("Input matrix 1 of order",m,"x",n)
m1=[list(map(int,input().split())) for _ in range(m)]
print("Input matrix 2 of order",p,"x",q)
m2=[list(map(int,input().split())) for _ in range(p)]
rm=[]
if n==q:
    for i in range(m):
        r=[]
        for j in range(q):
            c=0
            for k in range(n):
                c=c+m1[i][k]*m2[k][j]
            r.append(c)
        rm.append(r)
    print("Multiplied matrix is:",rm)
else:
    print("Wrong inputs")


