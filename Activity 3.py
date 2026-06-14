class UK:
    def capital(self):
        print("London")
    def language(self):
        print("English")
    def type(self):
        print("developed")
class Pakistan:
    def capital(self):
        print("Islamabad")
    def language(self):
        print("Urdu")
    def type(self):
        print("developing")
x=Pakistan()
y=UK()
for i in(x,y):
    i.capital()
    i.language()
    i.type()
        
