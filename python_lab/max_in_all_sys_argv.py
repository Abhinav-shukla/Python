import sys
l=sys.argv[1:]
print("Input values are:",l)
max=int(l[1])
for i in l:
    if int(i)>max:
        max=int(i)
print("Maximum number is",max)
