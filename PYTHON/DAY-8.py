class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

# Sample usage
my_car = Car("Hyundai", "i20", 2023)
print(my_car.display_info())
