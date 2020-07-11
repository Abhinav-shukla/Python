class students:
    def __init__(self):
        self.brand = 'HP'
        self.tool = 'Laptop'
        self.spec = self.laptop()

    def show(self):
        print(self.brand, self.tool)
        self.spec.show()

    class laptop:

        def __init__(self):

            self.ram = '8GB'
            self.cpu = 'i5'

        def show(self):

            print(self.ram, self.cpu)


x = students()
x.tool='Computer'
x.spec.cpu='i9'
x.spec.ram='16GB'
x.show()
