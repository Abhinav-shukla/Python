class computer:

    def __init__(self,cpu,ram):#one argument is the object or the instance itself
        # print('In init')
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print('The config is as: ',self.cpu,self.ram)


com=computer('i5','4GB')  #computer.__init__(com)  
com1=computer('ryzen','8GB')
com.config()
com1.config()