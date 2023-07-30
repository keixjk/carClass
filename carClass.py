class Car:
    def __(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed
    
    # Program
    def main():
        car = Car(2022, 'Example Make')

        # print
        print("Initial Speed:", car.get_speed())

        # Accelerate five times
        for _ in range(5):
            car.accelerate()
            print("Current Speed (Accelerating):", car.get_speed())

        # Brake 5 times
        for _ in range(5):
            car.brake()
            print("Current Speed (Braking):", car.get_speed())

