def newton_root(a):
    n1=a
    c=1
    n2=0.5*(n1+a/n1)
    while n1-n2>0.001:
        n1=n2
        c+=1
        n2=0.5*(n2+a/n2)
    return (n2,c)
n=float(input("Enter the number:"))
print("square root is:",newton_root(n))
