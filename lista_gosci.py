#lista gości
guest = []

#pętla uzupełniająca listę
for x in range(3):
    x=guest.append(input("Podaj imię osoby, którą chciałbyś zaprosić na przyjęcie : "))

print("Super! Poniżej lista zaproszonych osób! \n")
#wypisanie osób zaproszonych
for x in guest:
    print("Wysłałeś zaproszenie do :"+x)

#cofnięcie zaproszenia dla jednego z gości
print("Oooo Nie! " + guest[2] + " nie może przyjść :( \n")
absent=guest[2]
guest.remove(absent)

#zaktualizowana lista
for x in guest:
    print("Na przyjęcie przyjdzie "+x)

