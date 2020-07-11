# print([[i, j, k] for [i, j, k] in [[i for i in range(10)],[j for j in range(10)],[k for k in range(10)]]])
# x, y, z, n = list(map(int, input().split()))
# print([[i, j, k] for i in range(x+1) for j in range(y+1)
#        for k in range(z+1) if i+j+k != n])
# l = []
# s = []
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     l.append([name, score])
#     s.append(score)
# m = min(s)
# for i in l:
#     if i[1] == m:
#         l.remove(i)
#         s.remove(m)
# m = min(s)
# for i in l:
#     if i[1] == m:
#         print(i)
# l=[1,2,3,4,5,6]
# l.insert(0,78)
# print(l)

# l = []
# c = 0
# p = [0, 0]
# n = int(input())
# for _ in range(n):
#     name = input()
#     score = float(input())
#     l.append([score, name])
# for i in range(n):
#     for j in range(n-i-1):
#         if l[j][0] > l[j+1][0]:
#             l[j], l[j+1] = l[j+1], l[j]
# print(l)
# m = l[0][0]
# print(m)

# x,*y=input().split()
# y=list(map(int,y))
# print(x,y)

# import string as st
# print(st.ascii_lowercase)

# import string as st


# def swap_case(s):
#     new_str = ''
#     for i in s:
#         print(i)
#         if i in st.ascii_lowercase:
#             print(chr(ord(i)+32))
#         elif i in st.ascii_uppercase:
#             print('u')
#             new_str += chr(ord(i)-32)
#         else:
#             print('o')
#             new_str += i
#     print(new_str)


# #Replace all ______ with rjust, ljust or center.

# thickness = int(input()) #This must be an odd number
# c = 'H'

# #Top Cone
# for i in range(thickness):
#     print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Middle Belt
# for i in range((thickness+1)//2):
#     print((c*thickness*5).center(thickness*6))

# #Bottom Pillars
# for i in range(thickness+1):
#     print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Bottom Cone
# for i in range(thickness):
#     print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


# m, n = map(int, input().split())
# for i in range(m//2):
#     print('.|.'*((2*i) + 1).center(n, '-'))
# print('WELCOME'.center(n, '-'))

# def score(sub, string):
#     c = 0
#     for i in range(len(string) - len(sub)+1):
#         if sub == string[i:i+len(sub)]:
#             c += 1
#     return c


# def minion_game(string):
#     # your code goes here
#     l = []
#     for i in range(len(string)):
#         for j in range(i, len(string)):
#             if string[i:j+1] not in l:
#                 l.append(string[i:j+1])
#     # print(l)
#     print(len(l))
#     stuart = 0
#     kevin = 0
#     for i in l:
#         # print(i)
#         if i[0] in 'AEIOU':
#             kevin += score(i, string)
#         else:
#             stuart += score(i, string)
#     if stuart > kevin:
#         print('Stuart %d' % (stuart))
#     elif stuart == kevin:
#         print("Draw")
#     else:
#         print('Kevin %d' % (kevin))

#     # print('Kevin %d'%(kevin))
#     # print('Stuart %d'%(stuart))
# s = input()
# minion_game(s)


# def merge_the_tools(string, k):
#     # your code goes here
#     step = len(string)//k
#     print(step)
#     for i in range(step):
#         r=''
#         s = string[i*k:(i+1)*k]
#         for j in s:
#             if j not in r:
#                 r+=j
#         print(r)

# if __name__ == '__main__':
#     string, k = input(), int(input())
#     merge_the_tools(string, k)

# import re
# m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
# print(m.groupdict())

# import re
# m = re.match(r'(?P<user>\w+)@(?P<domain>\w+).(?P<extension>\w*)','abhinavshukla@gmail.com')
# print(m.groupdict())
# def print_formatted(number):
#     # your code goes here
#     l=len('{0:b}'.format(number))
#     for i in range(1,number+1):
#         print('{0:{l}d} {0:{l}o} {0:{l}x} {0:{l}b}'.format(i,l=l))
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)    