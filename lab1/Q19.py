class Engine:
    def __init__(self,type):
        self.type=type

    def start(self):
        print(f"{self.type} started")

    def stop(self):
        print(f"{self.type} stopped")

class Wheel:
    def __init__(self,type):
        self.type=type

    def start(self):
        print(f"{self.type} wheel started rolling")

    def stop(self):
        print(f"{self.type} wheel  stopped rolling")

class Car:
    def __init__(self,Engine_Instance,Wheel_Instance):
        self.engine=Engine_Instance
        self.wheel=Wheel_Instance
    def start_car(self):
        self.engine.start()
        print("Car started")
        self.wheel.start()


engine=Engine("Internal combustion engine")
wheel=Wheel("CEAT")
car=Car(engine,wheel)
car.start_car()