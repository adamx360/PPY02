def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def razy(a, b):
    return a * b


def dziel(a, b):
    return a / b


print("Wybierz co chcesz zrobic")

print("1 - dodac")
print("2 - odjac")
print("3 - pomnozyc")
print("4 - podzielic")

while True:
    choice = input("Wybierz dzialanie : ")

    if choice in ('1', '2', '3', '4'):
        l1 = float(input("Podaj 1 liczbe : "))
        l2 = float(input("Podaj 2 liczbe : "))

        if choice == '1':
            print(l1, "+", l2, "=", plus(l1, l2))

        elif choice == '2':
            print(l1, "-", l2, "=", minus(l1, l2))

        elif choice == '3':
            print(l1, "", l2, "=", razy(l1, l2))

        elif choice == '4':
            print(l1, "/", l2, "=", dziel(l1, l2))

        break

    else:
        print("Taka opcja nie istnieje w tym kalkulatorze")
