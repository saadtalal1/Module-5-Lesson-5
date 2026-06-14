from abc import ABC 
class x(ABC):
    def display_val(self):
        print(20)
    def abs_method(self):
        print("I'm an abstract method.")
class y(x):
    def abs_method(self):
        print("I'm an abstract method.")
a=y()
a.abs_method()
    
