l=list(map(int,input("Enter the numbers:").split()))
for i in range(len(l)-1):
    m=l[i]
    c=i
    for j in range(i+1,len(l)):
        if l[j]<m:
            m=l[j]
            c=j
    l[c],l[i]=l[i],l[c]
print("Sorted list is:",l)
