print('Witaj użytkowniku!')

password = input('Podaj hasło : \n')

filename = 'password.txt'
text = ''

with open(filename) as file_object:
    chars = file_object.readlines()

for char in chars:
    text += char.strip()


if text == password:
    print('jest ok')

else :
    print('dupa ')