# Create an class called car
# Give 5 attributes of the car class
# Give 5 methods of the car class
# Ensure the class is working as expected
# Push your code to github
class Car:
    def __init__ (self, brand, price, colour, miles, fuelguage):
        self.brand = brand
        self.price = price
        self.colour = colour
        self.miles = miles
        self.fuelguage = fuelguage

#prices increasing over the month
    def increase_price (self, increase_value):
        self.price = self.price + increase_value

# getting the speed of the car
    def set_speed(self, time):
        self.miles= self.miles/time
        pass
        
# calculating the price of some quantity of the car
    def total_price (self,quantity):
        self.price = self.price*quantity
        pass

# calculating fuelguage over the year
    def set_morefuel(self,fuelincrease_value):
        self.fuelguage = self.fuelguage * fuelincrease_value
        pass

#car has a new colour
    def set_newcolour(self, newcolour):
        return self.colour
        pass

#instatiation
Car1 = Car(brand= "Audi",price=1000000, colour= "Red",miles=89, fuelguage=700)
print("The car brand is:",Car1.brand)
print("The price of the car is:",Car1.price)
print(Car1.brand  + "has a" + Car1.colour  + "colour")
print(Car1.brand,"covers", Car1.miles , "miles")
print(Car1.brand ,"receives", Car1.fuelguage,"mL of fuel")

Car1.increase_price(500000)
print(Car1.brand +  "new price is",Car1.price)

Car1.set_speed(80)
print(Car1.brand  + "covers", Car1.miles, "miles/hr")

Car1.set_morefuel(30)
print(Car1.brand +"now receives", Car1.fuelguage ,"mL" +"over the years")

Car1.set_newcolour("Metallic Black")
print(Car1.brand +"is now" + Car1.colour)

