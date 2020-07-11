# # print(len([i for i in range(1,31) if i % 2 == 0]))
# i = 0
# while i < 5:
#     print(i)
#     i += 1
#     if i == 3:
#         break
# else:
#     print(0)
# print ('cd'.partition('cd'))
# l=[5,8,895,62,5,45,2,4]
# print(l.sort())
# print(l)

# x='15'
# print(x.split())
import string
l = string.ascii_lowercase
n = int(input())
for i in range(n):
    t = int(input())
    print(l[:t])
