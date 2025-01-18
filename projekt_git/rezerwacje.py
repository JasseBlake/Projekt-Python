import os,time



rezerwacja_file = "rezerwacja.json"


class Rezerwacja:

# Konstruktor klasy Rezerwacja
    def __init__(self, IdPasazer, IdLot):
        self.IdPasazer = int(IdPasazer)
        self.IdLot = int(IdLot)

# Metoda konwertująca obiekt na słownik
    def to_dict(self):
        return {
            "IdPasazer": self.IdPasazer,
            "IdLot": self.IdLot,
        }

# Metoda tworzy obiekt typu Rezerwacja z danych zawartych w słowniku
    @staticmethod
    def from_dict(data):
        return Rezerwacja(
            IdPasazer=data["IdPasazer"],
            IdLot=data["IdLot"]
        )

# Metoda wyświetlająca informacje o rezerwacji
    def wyswietl_informacjeRezerw(self):

        from DataRepo import odczytajSlownikZPliku
        Loty_Disc = odczytajSlownikZPliku("lot.json")
        Pasazer_Disc = odczytajSlownikZPliku("pasazer.json")

    # Uzyskanie obiektu pasażera i lotu na podstawie ID
        Rezerwujacy = Pasazer_Disc[self.IdPasazer]
        ZarezerwowanyLot = Loty_Disc[self.IdLot]

    # Wyświetlenie informacji o rezerwującym pasażerze i wybranym locie
        print("")
        print(f'Rezerwujący : {Rezerwujacy.imie} {Rezerwujacy.nazwisko}')
        print(f'Ma zarezerwowany lot o numerze: {ZarezerwowanyLot.numer_lotu}')
        print(f'Z: {ZarezerwowanyLot.miasto_odlotu} do {ZarezerwowanyLot.miasto_przylotu} ')
        print(f'O czasie {ZarezerwowanyLot.data_i_godzina_odlotu} ')
        print(f'Cena tego lotu to: {ZarezerwowanyLot.cena_biletu}')
        print("-" * 10)  # Separator dla lepszej czytelności



#Funkcja dodanie Rezerwacji
def DodajRezerwacje():
# Pobieranie aktualnych danych z plików
    from DataRepo import odczytajSlownikZPliku
    Loty_Disc = odczytajSlownikZPliku("lot.json")
    Pasazer_Disc = odczytajSlownikZPliku("pasazer.json")
    Rezerwacja_Disc = odczytajSlownikZPliku(rezerwacja_file)

#Jeżeli nie ma żadnych lotów to wpraca do menu
    if Loty_Disc == {}:
        print(f"Nie ma lotów wolnych")
        time.sleep(2)
        os.system('cls')
        #powrót do zarzadzaj rezerwacja
        return Rezerwacja_Disc,Loty_Disc
    else:
# Loty są - Wybór id lotu do rezerwacji
        while True:
            os.system('cls')
            print("WYBIERZ LOT DO REZERWACJI:")
            print("#" * 30)

# Wyświetlenie wszystkich obiektów z Loty_Disc, które mają przynajmniej 1 wolne miejsce
            for klucz, lot in Loty_Disc.items():
                if lot.dostepne_miejsca >=1:
                    print(f"Lot o kluczu {klucz}:")
                    lot.wyswietl_informacje()
                    print("-" * 30)  # Separator dla lepszej czytelności

            try:
                wybranyLot = int(input("Podaj klucz lotu, którego chcesz zarezerwować miejsce: "))
# Sprawdzenie czy wpsiany klucz istnieje i czy czy ma przynjamniej 1 wolne miejsce
                if wybranyLot in Loty_Disc and Loty_Disc[wybranyLot].wolne_miejsca >= 1:

                    break  # Wyjście z pętli, jeśli klucz jest poprawny

                else:
                    os.system('cls')
                    print("Podany klucz nie istnieje lub lot nie ma dostępnych miejsc. Spróbuj ponownie.")
                    time.sleep(2)
                    os.system('cls')
            except ValueError:
                os.system('cls')
                print("Proszę podać poprawny numer klucza (liczbę całkowitą).")
                time.sleep(2)
                os.system('cls')

    time.sleep(2)
    os.system('cls')


# Sprawdzenie czy w systemie są jacykolwiek pasazerowie
    # jak nie ma - powrót do menu
    if Pasazer_Disc == {}:
        print(f"Nie nie ludzi do tworzenia rezerwacji")
        time.sleep(2)
        os.system('cls')
        from main import zarzadzaj_rezerwacjami
        zarzadzaj_rezerwacjami()
    else:
    # jak jest - wyswietla wszystkie obiekty typu osoba i prosi wpisanie id wybranej osoby
        while True:
            os.system('cls')
            print("WYBIERZ OSOBE DLA KTÓREJ MA BYC REZERWACJA:")
            print("#" * 30)
# Wyświetlenie wszystkich obiektów w Pasazer_Disc - lista pasazerow

            for klucz, osoba in Pasazer_Disc.items():
                print(f"Lot o kluczu {klucz}:")
                osoba.wyswietl_informacjePas()
                print("-" * 30)  # Separator dla lepszej czytelności
# Wybor osoby do rezerwacji
            try:
                wybranaOsoba = int(input("Podaj klucz osoby dla której chcesz zarezerwować miejsce: "))

# Sprawdzenie, czy klucz istnieje w słownik dla wybranego pasazera

                if wybranaOsoba in Pasazer_Disc:
                    break  # Wyjście z pętli, jeśli klucz jest poprawny
                else:
                    os.system('cls')
                    print("Podany klucz nie istnieje . Spróbuj ponownie.")
                    time.sleep(2)
                    os.system('cls')
            except ValueError:
                os.system('cls')
                print("Proszę podać poprawny numer klucza (liczbę całkowitą).")
                time.sleep(2)
                os.system('cls')
    os.system('cls')

# Tworzenei obiektu typu Rezerwacja
    rezerwacja = Rezerwacja(wybranaOsoba,wybranyLot)
    print("Rezerwacja dokonana!")
    print("-" * 30)

# Redukcja o 1 wolnego miejsca w wybranym obiekcie Lot
    Loty_Disc[wybranyLot].wolne_miejsca-=1
# Zapsiaywanei zmian w Locie do pliku JSON
    from DataRepo import  dodaj_klucz, slownikToFile
    slownikToFile(Loty_Disc, "lot.json")

# Wyświetlanie informacji o stworzonej rezerwacji
    rezerwacja.wyswietl_informacjeRezerw()

    time.sleep(2)
    os.system('cls')

# Przypisywanie pierwszego wolnego klucza dla stworzonej rezerwacji
    Rezerwacja_Disc = dodaj_klucz(Rezerwacja_Disc,rezerwacja)
    Rezerwacja_Disc = dict(sorted(Rezerwacja_Disc.items()))
# Zapis zmian do pliku JSON
    slownikToFile(Rezerwacja_Disc, rezerwacja_file)
    return Rezerwacja_Disc,Loty_Disc


# Funkcja Usuń Rezerwacje

def UsunRezerwacja():
    os.system('cls')
# Pobieranie najnowszych danych z pliku JSON i dodanie ich do słwonika
    from DataRepo import odczytajSlownikZPliku
    Rezerwacja_Disc = odczytajSlownikZPliku(rezerwacja_file)

    while True:
        try:
            print("""------------------LISTA REZERWACJI:------------------

            """)
# Wyświetlenie listy dostepnych rezerwacji
            for klucz, rezerwacja in Rezerwacja_Disc.items():
                print(f"Pasazer o kluczu {klucz}:")
                rezerwacja.wyswietl_informacjeRezerw()
                print("-" * 30)
# Zapytanie o klucz rezerwacji która chcemy usunąć

            klucz = int(input("Podaj klucz (liczbę), który chcesz usunąć ze słownika: "))

# Sprawdź, czy klucz istnieje w słowniku

            if klucz in Rezerwacja_Disc:
# Usuwanie rezerwacji
                del Rezerwacja_Disc[klucz]
                print(f"Rezerwacja o kluczu {klucz} został usunięty.")

# Dodanie 1 do liczby wolnych miejsc ,ktora ta rezerwacja zajmowała
                from DataRepo import odczytajSlownikZPliku
                Loty_Disc = odczytajSlownikZPliku("lot.json")
                Loty_Disc[klucz].wolne_miejsca+=1

# Zapisywanei zmian do pliku JSON
                from DataRepo import slownikToFile
                slownikToFile(Rezerwacja_Disc, rezerwacja_file)
                return Rezerwacja_Disc
            else:
                print(f"Nie istnieje lot o kluczu:  {klucz} .")
        except ValueError:
            print("Wprowadzono nieprawidłową wartość. Klucz musi być liczbą.")
        os.system('cls')
