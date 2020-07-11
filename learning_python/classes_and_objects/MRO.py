class A:

    def __init__(self):
        print('This is init_1')

    def method1(self):
        print('This is method1.')

    def method2(self):
        print('This is method2.')


class B(A):

    def __init__(self):
        super().__init__()
        print('This is init_2')

    def method3(self):
        print('This is method3.')

    def method4(self):
        print('This is method4.')


x = B()
