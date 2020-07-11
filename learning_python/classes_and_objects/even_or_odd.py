class find:
    even = 0

    def check(self, num):
        if num % 2 == 0:
            self.even = 1

    def even_odd(self, num):
        self.check(num)
        if self.even == 1:
            print('It is a even number')
        else:
            print('It is a odd number')


x = find()
x.even_odd(10)
