pytanie = input("Jak masz na imię i nazwisko?")

print("Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie")
print("1 - oglądanie telewizji/filmów/seriali")
print("2 - czytanie książek/czasopism ")
print("3 - słuchanie muzyki ")
choice1 = input("Wybierz odp : ")
if choice1 in ('1', '2', '3'):
    if choice1 == '1':
        odp1 = "oglądanie telewizji/filmów/seriali"
    elif choice1 == '2':
        odp1 = "czytanie książek/czasopism"
    elif choice1 == '3':
        odp1 = "słuchanie muzyki"
else:
    odp1 = "nie ma takiej odpowiedzi"

print("W jakich okolicznościach czytasz książki najczęściej?")
print("1 - podczas podróży ")
print("2 - w czasie wolnym (po pracy, na urlopie)  ")
print("3 - podczas pracy/nauki (to ich element) ")
choice2 = input("Wybierz odp : ")
if choice2 in ('1', '2', '3'):
    if choice2 == '1':
        odp2 = "podczas podróży "
    elif choice2 == '2':
        odp2 = "w czasie wolnym (po pracy, na urlopie) "
    elif choice2 == '3':
        odp2 = "podczas pracy/nauki (to ich element) "
else:
    odp2 = "nie ma takiej odpowiedzi"

print("Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?")
print("1 - chęć poszerzenia wiedzy  ")
print("2 - czytanie mnie relaksuje/odpręża  ")
print("3 - fakt, że czytanie jest modne  ")
choice3 = input("Wybierz odp : ")
if choice3 in ('1', '2', '3'):
    if choice3 == '1':
        odp3 = "chęć poszerzenia wiedzy  "
    elif choice3 == '2':
        odp3 = "czytanie mnie relaksuje/odpręża  "
    elif choice3 == '3':
        odp3 = "fakt, że czytanie jest modne "
else:
    odp3 = "nie ma takiej odpowiedzi"

print("Po książki w jakiej formie sięgasz najczęściej?")
print("1 - papierowej (tradycyjnej) ")
print("2 - e-booki (książki elektroniczne) na komputerze  ")
print("3 - e-booki na tablecie/telefonie ")
choice4 = input("Wybierz odp : ")
if choice4 in ('1', '2', '3'):
    if choice4 == '1':
        odp4 = "papierowej (tradycyjnej)  "
    elif choice4 == '2':
        odp4 = "e-booki (książki elektroniczne) na komputerze "
    elif choice4 == '3':
        odp4 = "e-booki na tablecie/telefonie  "
else:
    odp4 = "nie ma takiej odpowiedzi"

print("Ile książek czytasz średnio w ciągu roku?")
print("1 - 0  ")
print("2 - żadnej w całości - jedynie fragmenty   ")
print("3 - 2 lub 3  ")
choice5 = input("Wybierz odp : ")
if choice5 in ('1', '2', '3'):
    if choice5 == '1':
        odp5 = "0 "
    elif choice5 == '2':
        odp5 = "żadnej w całości - jedynie fragmenty  "
    elif choice5 == '3':
        odp5 = "2 lub 3  "
else:
    odp5 = "nie ma takiej odpowiedzi"

print("Jak często średnio czytasz książki?")
print("1 - codziennie")
print("2 - raz w tygodniu  ")
print("3 - raz w miesiącu  ")
choice6 = input("Wybierz odp : ")
if choice6 in ('1', '2', '3'):
    if choice6 == '1':
        odp6 = "codziennie "
    elif choice6 == '2':
        odp6 = "raz w tygodniu  "
    elif choice6 == '3':
        odp6 = "raz w miesiącu  "
else:
    odp6 = "nie ma takiej odpowiedzi"

print("Po jakie gatunki książek sięgasz najczęściej?")
print("1 - kryminały/thrillery ")
print("2 - romanse ")
print("3 - psychologiczne  ")
choice7 = input("Wybierz odp : ")
if choice7 in ('1', '2', '3'):
    if choice7 == '1':
        odp7 = "kryminały/thrillery  "
    elif choice7 == '2':
        odp7 = "romanse   "
    elif choice7 == '3':
        odp7 = "psychologiczne "
else:
    odp7 = "nie ma takiej odpowiedzi"

# wyświetlanie pytań i odpowiedzi
print("pytanie: Jak masz na imię i nazwisko? odpowiedź:", pytanie)

print("pytanie: Najczęstszym sposobem spędzania wolnego czasu jest dla Ciebie:", odp1)
print("pytanie: W jakich okolicznościach czytasz książki najczęściej?:", odp2)
print("pytanie: Jeżeli spędzasz czas wolny czytając książki, jaki jest główny powód takiego wyboru?:", odp3)
print("pytanie: Po książki w jakiej formie sięgasz najczęściej?:", odp4)
print("pytanie: Ile książek czytasz średnio w ciągu roku?:", odp5)
print("pytanie: Jak często średnio czytasz książki?:", odp6)
print("pytanie: Po jakie gatunki książek sięgasz najczęściej?:", odp7)
