class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f"The car {self.name} is moving now!")

    def stop(self):
        self.speed = 0
        print("The car stopped!")

    def turn(self, direction):
        print("Car is turned on ", direction)

    def show_speed(self):
        print("Current speed = ", self.speed)

class TownCar(Car):
    def __init__(self, speed, color, name, is_police, passengers):
        super().__init__(speed, color, name, is_police)
        self.passengers = passengers

    def show_speed(self):
        if self.speed > 60:
            print("Overspeed message (>60)! Current speed = ", self.speed)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police, lifting_capacity):
        super().__init__(speed, color, name, is_police)
        self.lifting_capacity = lifting_capacity

    def show_speed(self):
        if self.speed > 40:
            print("Overspeed message (>40)! Current speed = ", self.speed)

class SportCar(Car):
    def __init__(self, speed, color, name, is_police, capacity):
        super().__init__(speed, color, name, is_police)
        self.capacity = capacity

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

a= Car(100, 'Blue', 'Lexus', False)
a.go(80)
a.turn('left')
a.show_speed()
a.stop()
a.show_speed()

a= TownCar(80, 'Green', 'Ford', False, 4)
a.go(80)
a.turn('right')
a.show_speed()
a.stop()
a.show_speed()

a= WorkCar(50, 'Red', 'MAN', False, 2000)
a.go(55)
a.turn('left')
a.show_speed()
a.stop()
a.show_speed()
