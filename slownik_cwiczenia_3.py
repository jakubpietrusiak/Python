#cwiczenie rzeki
#Stwórz słownik zawierający trzy ważne rzeki i kraje przez które przepływa dana
# rzeka

rivers ={'nil':'egipt','wisła':'polska','misouri':'stany zjednoczone ameryki'}
for key, value in rivers.items():
    print('Rzeka ' + key.title() + ' przepływa przez ' +value.title()+ '.\n' )

#wyświetlenie w pętli samych nazw krajów
for value in rivers.values():
    print(value.title())