class Cars():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def car_information(self):
        long_information = self.make + ' ' + self.model + ' ' + str(self.year)
        return  long_information.title()

    def read_odometer(self):
        print('Ten samochód ma przejechane dopiero ' + str(self.odometer) +
              '\n')

    def update_odometer(self , mileage):
        self.odometer = mileage

class Battery():
    def __init__(self,battery_size = 70):
        self.battery_size = battery_size

    def battery_information(self):
        print('Ten samochód ma akumulator o pojemności ' + str(
            self.battery_size) + ' kWh. ')

    def car_range(self):
        print('Zasięg tego auta to około 250 km.')

class ElectricCars(Cars):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()



