l=list(map(str,input("Input the words:").split(" ")))
m=[]
for i in l:
    c=0
    for j in i:
        c+=1
    m.append(c)
print(m)
