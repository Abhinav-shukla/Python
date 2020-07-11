class ABC:
    count = 0

    def __init__(self, num):
        ABC.count += 1
        self.var = num
        print('The value for %d id %d' % (ABC.count, num))

    def __del__(self):
        print('This is del for %d object i.e. %d.' % (ABC.count, self.var))
        ABC.count -= 1


x = ABC(15)
y = ABC(16)
z = ABC(17)
del z
del y
del x
