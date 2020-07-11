import math
roman={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
l=[1,5,10,50,100,500,1000]
def closest(n):
    i=0
    while l[i]<n:
        i+=1
    j=len(l)-1
    while l[j]>n:
        j-=1
    return (l[j],l[i])
def chunk(n):
    if n in l:
        return roman[n]
    else:
        p1,p2=map(int,closest(n))
        r=''
        if (p2-l[(l.index(p1)-1)])==n:
            while n!=p2:
                r=r+roman[l[(l.index(p1)-1)]]
                n=n+l[(l.index(p1)-1)]
            r=r+roman[p2]
        else:
            r=r+roman[p1]
            while n!=p1:
                r=r+roman[l[l.index(p1)-1]]
                n=n-l[(l.index(p1)-1)]
        # if n-p1 <= p2-n:
        #     v=p1
        #     v1=p2
        # else:
        #     v=p2
        #     v1=p1
        # if v<n:
        #     r=r+roman[v]
        #     c=n-v
        #     for i in range(c):
        #         r=r+roman[1]
        # elif v>n:
        #     while v!=n:
        #         r=r+roman[v1]
        #         n=n+v1
        #     r=r+roman[v]
    return r   
n=int(input("Enter the number:"))
final=''
m=n
lc=[]
i=0
c=0
if n in l:
    final=chunk(n)
else:
    while m!=0:
        c=m%10
        c=c*math.pow(10,i)
        if c!=0:
            lc.append(int(c))
        i+=1
        m=m//10
    lc=lc[::-1]
    for i in lc:
        final=final+chunk(i)
print(final)

