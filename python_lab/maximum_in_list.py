l=list(map(int,input("Enter the numbers:").split()))
m=l[0]
for i in l:
    if m<i:
        m=i
print("maximum is:",m)
