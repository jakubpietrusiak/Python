class Restaurant():

    def __init__(self, restaurant_name , cousine_type, open_hour , closed_hour ):
        self.name = restaurant_name
        self.type = cousine_type
        self.open = open_hour
        self.close = closed_hour

    def describe_restaurant(self):
        print('Ta restauracja nazywa się : ' + self.name.title())
        print('Preferuje kuchnię ' + self.type + '\n')

    def open_restaurant(self):
        print('Jest czynna w godzinach ' + str(self.open) +  '-' + str(self.close) )



my_restaurant = Restaurant('kapiszon' , 'polska tradycyjna' , '12' , '20')
your_restaurant = Restaurant('wółczykij', 'fast food', '10' , '24')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()

