#Cwiczenie
#tworzymy listę kilku użytkowników "serwisu". Dla każdego wyświetlamy powitanie. Dla jednego z nich specjalne

users = ['admin','ruperst2232','jolie232','wqeqw22','jeremiasz','saasawe12321_9']

for user in users:
    if user == 'admin':
        print('Witaj Administratorze! Chcesz przejrzeć raport?')
    else:
        print('Witaj '+user.title()+ ', dzięki za kolejne odwiedziny !')

print('\n')

#dodajemy warunek sprawdzający czy lista nie jest pusta

if len(users) < 1:
    print('Halo halo!Lista uzytkowników jest pusta')
else:
    print(len(users))

print('\n')

#dodawanie nowego użytkownika z sprawdzeniem czy taki nie istnieje już
new_user =input('Wprowadź nowego użytkownika : \n')
if new_user in users:
    print('Jest już taki użytkownik!')
else :
    users.append(new_user)
    print('Dodano nowego użytkownika do listy pomyślnie')

print(users)

#trzeba jeszcze ustawić że duża i mala litera nie ma znaczenia gdy chodzi i nazwę
