class myclass():
    # Private Variable
    __privateVar = 28
    # Private Method
    def __privateMeth(self):
        print("I am inside myclass")
    # Function to print value of the private variable
    def hello(self):
        print("Private Variable value:", myclass.__privateVar)

# Object Creation and method call
obj1 = myclass()
obj1.hello()
obj1.__privateMeth
