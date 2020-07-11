"""If a bird swims like a duck, it quacks like a duck, it flies like a duck then it is a duck"""
class PyCharm:
    def execute(self):
        print('Compiling')
        print('Wait')

class MyEditor:
    def execute(self):
        print('Checking spellings')
        print('Checking syntax')
        print('Compilation complete')

class laptop:
    
    def code(self,ide):
        ide.execute()
ide=PyCharm()
ide=MyEditor()
test=laptop()
test.code(ide)