class Pycharm:
    def execute(self):
        print("Compiling")
        print("Running")

class MyEditor:
    #should have the execute
    def execute(self):
        print("Spell Check")
        print("Convention Check")
        print("Compiling")
        print("Running")
        

class Laptop:
    def code(self,ide):
        ide.execute()

#The class is passed as the object    
ide=MyEditor()
lap1=Laptop()

#The class object is passed as the argument 
lap1.code(ide)