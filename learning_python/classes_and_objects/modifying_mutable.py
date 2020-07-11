class FilterNum:
    odd=[]
    even=[]
    def __init__(self,num):
        if num % 2 == 0:
            FilterNum.even.append(num)
        else:
            FilterNum.odd.append(num)
n=FilterNum(21)
n=FilterNum(22)
n=FilterNum(11)
n=FilterNum(23)
n=FilterNum(1)
n=FilterNum(542)
n=FilterNum(141)
n=FilterNum(23)
print(FilterNum.odd)
print(FilterNum.even)
