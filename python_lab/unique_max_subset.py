n=int(input("Enter number of sublist:"))
l=[set(map(int,input("Input the sublist:").split())) for _ in range(n)]
print(l)
m=[]
for i in l:
    m.append(len(i))
print(m)
print("Max len at index:",m.index(max(m)))
