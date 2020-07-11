h,l=map(int,input("Enter number of heads and legs:").split())
r=2*h-l/2
m=h-r
if l%2!=0 or m<=0 or r<=0:
    print("No solution")
else:
    print("Number of rabits and chickens are:",int(r),int(m))
