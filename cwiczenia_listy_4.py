#Cwiczenie 1
#Zrób za pomocą pętli for odliczanie od 1 do 20. Sprawdz najmniejsze, najwieksze liczby z tablicy. Oraz zsumuj je

numbers = list(range(1,21))
for number in numbers:
    print(number)

print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list(range(1,21,2)) #nieparzyste liczby z zakresu 1 do 20
for odd_number in odd_numbers:
    print(odd_number)

cubes = [] #sześcian liczb od 3 do 30
for value in range(3,30):
    cube = value **3
    cubes.append(cube)

print(cubes)
for cube in cubes:
    print(cube)

cubes = [value **3 for value in range(3,30)] # lista składana!!!!! bardzo ważne !!!
print(cubes)