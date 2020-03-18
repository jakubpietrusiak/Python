class Login():

    def __init__(self,user_name,from_where,user_password):
        self.user = user_name
        self.city = from_where
        self.password = user_password

    def describe_user(self):
        print('Twój nick to : ' + self.user.title())
        print('Mieszkasz w : ' + self.city.title())

    def input_password(self):
        self.password = input('Podaj swoje hasło \n')
        print(self.password)


user1 = Login('kaziuki','przasnysz','')
user1.describe_user()
user1.input_password()

user2 = Login('bobcio234','losice','')
user2.describe_user()
user2.input_password()