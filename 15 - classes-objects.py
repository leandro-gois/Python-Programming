# Creating a simple class and objects
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
    
    def start(self):
        return f"The {self.color} {self.brand} is starting!"

# Create objects from the class
my_car = Car("Toyota", "silver")
friend_car = Car("Honda", "blue")

print(my_car.start())
print(f"My car: {my_car.brand}")
print(f"Friend's car: {friend_car.color}")
