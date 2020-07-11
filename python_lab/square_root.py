def newton_sqrt(a,k):
    n=a
    for i in range(k):
        n=0.5*(n +a/n)
    return n
a,k=map(int,input("Enter number and the frequency:").split())
print("Square root:",newton_sqrt(a,k))
