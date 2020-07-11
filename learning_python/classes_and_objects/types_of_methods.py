# #constructor allocates size to the objects.
# there are three types of methods:
#     instance / object method
#     class method
#     static method


class students:

    school = 'Shurya institution'

    def __init__(self):  # instance methods

        self.marks = 100
        self.name = 'Brocode'

    @classmethod        #class_methods
    def detail(cls):

        print('He belongs to the '+cls.school)
    
    @staticmethod       #static_methods
    def info():
        print('It is the best institute of INDIA.')
    
s1 = students()
print(s1.marks, s1.name)
students.detail()
students.info()
