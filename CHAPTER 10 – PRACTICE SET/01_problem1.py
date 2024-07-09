class Programmer:
    company="Microsoft"

    def __init__(self,name ,salary, pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=Programmer("Ansh", 1200000, 125001)
print(p.name, p.salary, p.pin, p.company)

h=Programmer("Harry", 1200000, 125001)
print(h.name, h.salary, h.pin, h.company)