class Vehicle:
    def __init__(self,make,model):
        self.make=make
        self.model=model
    def drive(self):
        print(f"driving the {self.make} and {self.model}")

class Car (Vehicle):
    # def __init__(self,make,model):
    #     self.make=make
    #     self.model=model
    def drive(self):
        print(f"driving {self.make} and {self.model} car")


car1=Car(233,"suv")
car1.drive()