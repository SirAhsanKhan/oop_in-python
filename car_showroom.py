class Car:
    def __init__(self):
        self.brand = input("Enter your brand: ")
        self.model = input("Enter your model: ")
        self.price = float(input("Enter your price in $: "))

class ElectricCar(Car):
    def __init__(self, battery_size):
        super().__init__()
        self.__battery_size = battery_size

    def get_battery_size(self):
        return self.__battery_size
    
    def all_info(self):
        return f"{self.brand} {self.model} | Battery: {self.__battery_size} kWh | Price: ${self.price}"


my_car = ElectricCar()
print(my_car.all_info())