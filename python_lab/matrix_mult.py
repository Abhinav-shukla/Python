x=[[1, 7, 3], [3, 5, 6], [6, 8, 9]]
y=[[1, 1, 1, 2], [6, 7, 3, 0], [4, 5, 9, 1]]
print("Matrix 1 is:",x)
print("Matrix 2 is:",y)
print(len(y))
rm=[]
for i in range(len(x)):
    r=[]
    for j in range(len(y[1])):
        c=0
        for k in range(len(y)):
            c=c+x[i][k]*y[k][j]
        r.append(c)
    rm.append(r)
print("Multiplied matrix is:",rm)

