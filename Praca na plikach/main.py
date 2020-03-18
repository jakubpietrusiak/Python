with open('py_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

filename = 'py_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

number = input('Podaj jakis numer \n')

if number in pi_string:
    print('Twoja liczba znajduje się w pierszych 100 cyfrach liczby pi')

else :
    print('Twojej liczby nie ma wśród pierwszych 100 liczb... ')