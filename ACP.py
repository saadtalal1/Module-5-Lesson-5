class BMW:
    def mileage(self):
        print("mileage: 1000 km")

    def max_speed(self):
        print("BMW max speed: 250 km/h")

class Ferrari:
    def mileage(self):
        print("mileage: 1250 km")

    def max_speed(self):
        print("Ferrari max speed: 340 km/h")

car_bmw = BMW()
car_ferrari = Ferrari()

for car in (car_bmw, car_ferrari):
    car.mileage()
    car.max_speed()