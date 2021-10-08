class Car(object):

    def __init__(self, model, color, company, speedLimit):
        self.color=color
        self.model=model
        self.company=company
        self.speedLimit=speedLimit

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelerate(self):
        print("Accelerating")
        "Accelerating related funcionality here"

    def change_gear(self,gear_type):
        print("Gear changed")
        "Gear related funcionality here"

    audi = Car("Audi A6", "red", "Audi", 200)

