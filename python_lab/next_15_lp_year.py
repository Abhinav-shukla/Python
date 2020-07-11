def lp_year(n):
    if (n%400==0) or (n%4==0 and n%100!=0):
        return True
    else:
        return False
n=int(input("Enter the year:"))
c=0
while c!=15:
    if lp_year(n):
        print(n)
        c+=1
    n+=1
    
