class number:

    flag = 0

    def condition(self, num):

        if num % 2 == 0:
            self.flag == 1

    def check(self, num):

        self.condition(num)

        if self.flag == 1:
            print('Even number')
        else:
            print('Odd number')


x = number()
x.check(21)
