class Person:
    #<__main__.Person object at 0x00000230AF0037C0> memory address of that instance.
    def __init__(self,firstname,secondname):
        self.f_name=firstname
        self.s_name=secondname
        
    def __str__(self) -> str:
        return f"Person({self.f_name},{self.s_name})"
    
p=Person("Thinley","Norbu")
print(p)
    