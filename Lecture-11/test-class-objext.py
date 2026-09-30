class Car:
    wheels = 4

    def __init__(self, make, modle, year):
        self.make = make
        self.modle = modle
        self.year = year

        def start_engine(self):
            return f"The engine of the {self.year} {self.make} {self.modle} is now running."

            def stop_engine(self):
                return f"The engine of the {self.year} {self.make} {self.modle} is now off."

my_car = Car("Toyota", "Corolla", 2020)

print(my_car.make)
print(my_car.modle)
print(my_car.year)

print(my_car.start_engin())
print(my_car.stop_engin())
        