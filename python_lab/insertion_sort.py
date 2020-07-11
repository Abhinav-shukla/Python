l=list(map(int,input("Input the list:").split()))
for i in range(1,len(l)):
    j=i-1
    temp=l[i]
    while j!=-1 and l[j]>temp:
        l[j+1]=l[j]
        j-=1
    l[j+1]=temp
print(l)
