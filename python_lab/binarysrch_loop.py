l=list(map(int,input("Enter the numbers:").split()))
n=int(input("Enter the number to search:"))
m=sorted(l)
b=0
e=len(l)-1
c=0
while b < e:
    mid=(b+e)//2
    if n==m[mid]:
       c=mid
       break
    elif m[mid]>n:
        e=mid-1
    elif m[mid]<n:
        b=mid+1
print("Item found at:",l.index(m[c]))
