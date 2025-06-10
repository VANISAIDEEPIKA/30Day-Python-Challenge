class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def display_info(self):
        return f"{super().display_info()} with {self.battery_capacity}kWh battery"


# Sample usage
my_ev = ElectricCar("Tesla", "Model 3", 2022, 75)
print(my_ev.display_info())
