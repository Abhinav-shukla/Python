l=list(map(int,input("Enter numbers:").split()))
x=int(input("Enter the number to be searched:"))
c=0
for i in l:
    if i==x:
        print("Item found at index",l.index(i))
        c+=1
if c==0:
    print("Item not found")
