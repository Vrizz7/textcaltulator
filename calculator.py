def dodawanie():
    x = int(input("Podaj pierwsza liczbe"))
    y = int(input("Podaj druga liczbe"))
    wynik = x + y
    return wynik

def odejmowanie():
    x = int(input("Podaj pierwsza liczbe"))
    y = int(input("Podaj druga liczbe"))
    wynik = x - y
    return wynik

def mnozenie():
    x = int(input("Podaj pierwsza liczbe"))
    y = int(input("Podaj druga liczbe"))
    wynik = x * y
    return wynik

def dzielenie():
    x = int(input("Podaj pierwsza liczbe"))
    y = int(input("Podaj druga liczbe"))
    wynik = x / y
    return wynik

def menu():
    print ("Wybierz dzialanie \n 1 Dodawanie \n 2 Odejmowanie \n 3 Mnozenie \n 4 Dzielenie")
    choice = int(input())
    if choice == 1:
        print(dodawanie())
        return menu()
    if choice == 2:
        print(odejmowanie())
        return menu()
    if choice == 3:
        print(mnozenie())
        return menu()
    if choice == 4:
        print (dzielenie())
        return menu()

print (menu())