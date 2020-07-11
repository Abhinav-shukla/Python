def binary(b,e):
    m=(b+e)//2
    if item==l[m]:
        return m
    elif item<l[m]:
        return binary(b,m-1)
    else:
        return binary(m+1,e)
m=list(map(int,input("Enter list:").split()))
l=sorted(m)
item=int(input("Enter number:"))
print("item found at",m.index(l[binary(0,len(l)-1)]))
