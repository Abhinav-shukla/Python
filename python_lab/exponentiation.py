x,y=map(int,input("Enter number and power:").split())
n=1
for _ in range(y):
    n=n*x
print("Answer is:",n)
