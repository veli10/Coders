class Car:
    car_count = 0
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

        Car.car_count += 1
        
    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)
        
    def display_car_count():
        print("Total number of cars:", Car.car_count)

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Tesla", "Model S", 2022)

car1.display_info()
car2.display_info()
Car.display_car_count()
