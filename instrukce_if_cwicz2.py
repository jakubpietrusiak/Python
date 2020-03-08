#cwiczenie
# liczby porządkowe w języku angielskim zazwyczaj kończą się na "th" wyjątkiem
# jest 1,2,3. Utwórz listę przechowującą liczby od 1 do 9. Przeprowadź iterację
# przez listę. Wykorzystaj if-elif-else

numbers = list(range(1,10))


for number in numbers:
    if number == 1:
        print('1st')
    elif number ==2:
        print('2nd')
    elif number ==3:
        print('3rd')
    else:
        print(str(number) + 'th')
