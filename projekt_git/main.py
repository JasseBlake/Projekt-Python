import os, time

pasazer_file = "pasazer.json"
lot_file = "lot.json"
rezerwacja_file = "rezerwacja.json"

# Słowniki do przechowywania danych z plików JSON
Loty_Disc = {}
Pasazer_Disc = {}
Rezerwacja_Disc = {}




# Pobieranie danych z plików JSON i przypisywanie ich do słowników
def odswiez_slowniki():
    from DataRepo import odczytajSlownikZPliku

    global Loty_Disc, Pasazer_Disc, Rezerwacja_Disc

    Loty_Disc = odczytajSlownikZPliku(lot_file)
    Pasazer_Disc = odczytajSlownikZPliku(pasazer_file)
    Rezerwacja_Disc = odczytajSlownikZPliku(rezerwacja_file)


############################ MENU #########################################

# MENU GŁOWNE

def menuGlowne():
    # odswieza dane
    odswiez_slowniki()
    # Menu opcji

    while True:
        print("""Witaj w systemie: W69138 !
        =========================
        Wybierz opcje:

        1. Zarządzaj lotami
        2. Zarządzaj pasażerami
        3. Zarzadzaj rezerwacjami
        4. Wyjdż z programu
        """)

        choice = input("Wprowadz numer wybranej opcji: ")
        # zarzadzaj lotami
        if choice == "1":
            zarzadzaj_lot()
            break
        # zarzadzaj pasazerami
        elif choice == "2":
            zarzadzaj_pasazerami()
            break
        # zarzadzaj rezerwacajmi
        elif choice == "3":
            zarzadzaj_rezerwacjami()
            break
        # Wyjdz z programu
        elif choice == "4":
            exit()
        else:
            os.system('cls')
            print("!!! Wprowadź poprawny numer opcji !!!")
            time.sleep(2)
            os.system('cls')

# ZARZADZAJ LOTAMI MENU

def zarzadzaj_lot():
    from loty import DodajLot
    global Loty_Disc
    os.system('cls')

# MENU WYBORU
    while True:
        print("""Zarządzanie lotami: !
        =========================
        Wybierz opcje:

        1. Wyświetl wszystkie loty
        2. Dodaj lot
        3. Usuń lot
        4. Wróć
        """)

        choice = input("Wprowadz numer wybranej opcji: ")
# Wyświetl wszystkie loty

        if choice == "1":
            if Loty_Disc=={}:
                print(f"Nie ma danych do poakzania")
                time.sleep(2)
                os.system('cls')
                zarzadzaj_lot()
            else:

                while True:
# Wyświetlenie wszystkich obiektów w Loty_Disc
                    for klucz, lot in Loty_Disc.items():
                        print(f"Lot o kluczu {klucz}:")
                        lot.wyswietl_informacje()
                        print("-" * 30)  # Separator dla lepszej czytelności

                    print("Jezeli chcesz wrocic wpisz 'back'")
                    x = input("Wprowadz : ")
                    if x in ['back', 'BACK']:
                        zarzadzaj_lot()
                        break
                    else:
                        print("Nieprawidłowy wybór, spróbuj ponownie.")


# #########################
# Dodaj lot
        elif choice == "2":

            os.system('cls')
            while True:
                 print("Czy napewno chcesz dodać lot? y -TAK , n- NIE")
                 x = input("Wprowadz 'y' albo 'n' : ")
                 if x in ['n', 'N']:
                     os.system('cls')
                     zarzadzaj_lot()
                     break

                 elif x in ['y', 'Y']:
                    os.system('cls')
                    #TUTAJ JESZCZE SPRAWDZ

                    #Loty_Disc= DodajLot()
                    Loty_Disc=DodajLot()
                    print()
                    #os.system('cls')
                    zarzadzaj_lot()

                    break
                 else:
                    os.system('cls')
                    print("!!! Wprowadź poprawną odpowiedz !!!")
                    time.sleep(2)
                    os.system('cls')

#                    # break
# Usuwanie lotu
        elif choice == "3":
            from loty import UsunLot
            Loty_Disc=UsunLot()
            break

        elif choice == "4":  # Wróć
            os.system('cls')
            menuGlowne()
            break
        else:
            os.system('cls')
            print("!!! Wprowadź poprawny numer opcji !!!")
            time.sleep(2)
            os.system('cls')





# ZARZADZAJ PASAZERAMI MENU

def zarzadzaj_pasazerami():
    from pasazer import DodajPasazer
    global Pasazer_Disc
    os.system('cls')

# MENU WYBORU
    while True:
        print("""Zarządzanie pasazerami: !
        =========================
        Wybierz opcje:

        1. Wyświetl wszystkich pasazerow
        2. Dodaj pasazera
        3. Usuń pasazera
        4. Wróć
        """)

        choice = input("Wprowadz numer wybranej opcji: ")

# Jezeli nie ma pasazerow - przekierowanie do menu zarzadzaj pasazerami

# Wyswietl wszsytkich pasazerow - opcja
        if choice == "1":
            if Pasazer_Disc=={}:
                print(f"Nie ma danych do pokazania")
                time.sleep(2)
                os.system('cls')
                zarzadzaj_pasazerami()
            else:

                while True:
                    for klucz, pasazer in Pasazer_Disc.items():
                        print(f"Pasazer o kluczu {klucz}:")
                        pasazer.wyswietl_informacjePas()
                        print("-" * 30)  # Separator dla lepszej czytelności

                    print("Jezeli chcesz wrocic wpisz 'back'")
                    x = input("Wprowadz : ")
                    if x in ['back', 'BACK']:
                        zarzadzaj_pasazerami()
                        break
                    else:
                        print("Nieprawidłowy wybór, spróbuj ponownie.")

# Dodaj pasazera - opcja
        elif choice == "2":

            os.system('cls')
            while True:
                 print("Czy napewno chcesz dodać pasazera? y -TAK , n- NIE")
                 x = input("Wprowadz 'y' albo 'n' : ")
                 if x in ['n', 'N']:
                     os.system('cls')
                     zarzadzaj_pasazerami()
                     break

                 elif x in ['y', 'Y']:
                    os.system('cls')
                    Pasazer_Disc=DodajPasazer()
                    zarzadzaj_pasazerami()

                    break
                 else:
                    os.system('cls')
                    print("!!! Wprowadź poprawną odpowiedz !!!")
                    time.sleep(2)
                    os.system('cls')

# Usuwanie lotu - opcja
        elif choice == "3":
            pass
            from pasazer import UsunPasazer
            Pasazer_Disc=UsunPasazer()
            #break

# Powrót do menu głowne
        elif choice == "4":
            os.system('cls')
            menuGlowne()
            break
        else:
            os.system('cls')
            print("!!! Wprowadź poprawny numer opcji !!!")
            time.sleep(2)
            os.system('cls')




# ZARZADZAJ REZERWACJAMI MENU

def zarzadzaj_rezerwacjami():
    from rezerwacje import DodajRezerwacje
    global Rezerwacja_Disc
    os.system('cls')

# MENU WYBORU
    while True:
        print("""Zarządzanie rezerwacjami: !
            =========================
            Wybierz opcje:

            1. Wyświetl wszystkich rezerwacje
            2. Dodaj rezerwacje
            3. Usuń rezerwacje
            4. Wróć
            """)

        choice = input("Wprowadz numer wybranej opcji: ")
        ############################

# Wyświetl wszystkie rezerwacje - opcja

        if choice == "1":
            if Rezerwacja_Disc == {}:
                print(f"Nie ma danych do pokazania")
                time.sleep(2)
                os.system('cls')
                zarzadzaj_rezerwacjami()
            else:
                os.system('cls')
                while True:
    # Wyświetlenie wszystkich rezerwacji
                    for klucz, rezerwacja in Rezerwacja_Disc.items():
                        print(f"Rezerwacja o kluczu {klucz}:")
                        rezerwacja.wyswietl_informacjeRezerw()
                        print("-" * 30)  # Separator dla lepszej czytelności

# Powót - jezeli chcesz wprocic -wpisz back
                    print("Jezeli chcesz wrocic wpisz 'back'")
                    x = input("Wprowadz : ")
                    if x in ['back', 'BACK']:
                        zarzadzaj_rezerwacjami()
                        break
                    else:
                        print("Nieprawidłowy wybór, spróbuj ponownie.")



# Dodaj pasazera - opcja
        elif choice == "2":
            os.system('cls')
            while True:
                print("Czy napewno chcesz dodać pasazera? y -TAK , n- NIE")
                x = input("Wprowadz 'y' albo 'n' : ")
                if x in ['n', 'N']:
                    os.system('cls')
                    zarzadzaj_rezerwacjami()
                    break

                elif x in ['y', 'Y']:
                    os.system('cls')
                    Rezerwacja_Disc,Loty_Disc = DodajRezerwacje()
                    zarzadzaj_rezerwacjami()

                    break
                else:
                    os.system('cls')
                    print("!!! Wprowadź poprawną odpowiedz !!!")
                    time.sleep(2)
                    os.system('cls')


# Usuwanie lotu - opcja
        elif choice == "3":
            from rezerwacje import UsunRezerwacja
            Rezerwacja_Disc = UsunRezerwacja()
    # Powrót do menu głownego - opcja
        elif choice == "4":  # Wróć
            os.system('cls')
            menuGlowne()
            break
        else:
            os.system('cls')
            print("!!! Wprowadź poprawny numer opcji !!!")
            time.sleep(2)
            os.system('cls')


############################ FIRST RUN #########################################

#Wyswietla MENU GLOWNE
menuGlowne()
