A= [[55, 65, 49, 5], [98, 68, 18, 12],[90, 107, 66, 21] ]
x=list(zip(*A))
for i in x:
    print(max(i))
