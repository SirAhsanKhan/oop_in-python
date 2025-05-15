#create a class car with attribure brand and model

class Car:
    brand : str = "toyota" 
    model : int = 2019
    
print(Car.brand)  
print(Car.model)

# but we cant change its values  lie if we want to change toyota to benz we cant

#to slove this we will create class like this

# lets add functionality that shows full name of car
class Car:
    total_car = 0

    def __init__(self, brand, model):  # Constructor method
        self.brand = brand   # self is used to assign values to the instance
        self.model = model   # of the class Car
        Car.total_car += 1

    def fuel_type(self):
        return "diesel or petrol"
    
    # static method implementation
    @staticmethod
    def staticMethod():
        return 6 + 6
    
    #Inheritance & Encapsulate

class ElectricCar(Car): # while inheriting we are encapsulating battery_size 
    def __init__(self, battery_size :int , brand , model):
        super().__init__(brand , model)
        self.__battery_size = battery_size

    def fuel_type(self):
        return "Electric battery" # this is polymorphism
    
    def get_battery_size(self):
       return  self.__battery_size 

    def full_name(self):
        return f"{self.brand} {self.model} {self.__battery_size}"
    
        
my_tesla = ElectricCar(85,"tesla","S")
my_Kia = Car("Kia","sportage")

#using same function with different out put and objects
# print(my_tesla.fuel_type())
# print(my_Kia.fuel_type())

#   #Accessing the object's attributes
# print(my_Kia.brand)
# print(my_Kia.model)
# print(my_tesla.full_name())
# print(my_tesla.get_battery_size())
# print(Car.total_car)

#print static method

print(isinstance(my_Kia, Car)) # true 
print(isinstance(my_Kia, ElectricCar)) #false

print(isinstance(my_tesla, Car)) # true 
print(isinstance(my_tesla, ElectricCar)) #true


class battery:
    def battery_info(self) :
        return "this is battery"

class engine:
    def engine_info(self) :
        return "this is engine"
    
class New_model(Car, engine, battery):
    pass

my_new_car = New_model("tesla", "S")
print(my_new_car.battery_info())
print(my_new_car.engine_info())