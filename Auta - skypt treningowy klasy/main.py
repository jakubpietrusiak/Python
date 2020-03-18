from class_auta import *

print('Moje spalinowe auta : ')
car1 = Cars('audi','a4','2016')
print(car1.car_information())
car1.update_odometer(23000)
car1.read_odometer()

car2 = Cars('vovlo','V60 Polestar','2015')
print(car2.car_information())
car2.update_odometer(56000)
car2.read_odometer()

print('Moje elektryczne auta : ')

#przykład z dziedziczeniem

tesla = ElectricCars('tesla','model s','2016')
print(tesla.car_information())
tesla.battery.battery_information()
tesla.battery.car_range()