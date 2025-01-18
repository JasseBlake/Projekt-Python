from datetime import datetime, timedelta
import time ,os


lot_file= "lot.json"

class Lot:
#konstruktor klasy lot
    def __init__(self, numer_lotu, miasto_odlotu, miasto_przylotu, data_i_godzina_odlotu,czas_lotu,data_i_godzina_przylotu
                 ,cena_biletu, dostepne_miejsca,wolne_miejsca):
        self.numer_lotu = numer_lotu
        self.miasto_odlotu = miasto_odlotu
        self.miasto_przylotu = miasto_przylotu
        self.data_i_godzina_odlotu = data_i_godzina_odlotu
        self.czas_lotu = timedelta(minutes=czas_lotu) if isinstance(czas_lotu, int) else czas_lotu
        self.data_i_godzina_przylotu = data_i_godzina_przylotu
        self.cena_biletu = cena_biletu
        self.dostepne_miejsca = dostepne_miejsca
        self.wolne_miejsca = wolne_miejsca


# Metoda konwertująca obiekt na słownik

    def to_dict(self):
        return {
            "numer_lotu": self.numer_lotu,
            "miasto_odlotu": self.miasto_odlotu,
            "miasto_przylotu": self.miasto_przylotu,
            "data_i_godzina_odlotu": self.data_i_godzina_odlotu.isoformat(),
            "czas_lotu": self.czas_lotu.total_seconds() // 60,  # Zapisujemy czas lotu w minutach
            "data_i_godzina_przylotu": self.data_i_godzina_przylotu.isoformat(),
            "cena_biletu": self.cena_biletu,
            "dostepne_miejsca": self.dostepne_miejsca,
            "wolne_miejsca": self.wolne_miejsca,
        }

#metoda wyświetl dla klasy Lot
    def wyswietl_informacje(self):
        print(f"Lot numer: {self.numer_lotu}")
        print(f"Odlot z: {self.miasto_odlotu} do: {self.miasto_przylotu}")
        print(f"Data i czas odlotu: {self.data_i_godzina_odlotu.date()} {self.data_i_godzina_odlotu.time()}")
        print(f"Data i czas przylotu: {self.data_i_godzina_przylotu.date()} {self.data_i_godzina_przylotu.time()}")
        print(f"Cena biletu: {self.cena_biletu} PLN")
        print(f"Dostępne miejsca: {self.dostepne_miejsca}")
        print(f"Wolne miejsca: {self.wolne_miejsca}")


#Funkcja dodawania lotu
def DodajLot():

    numer_lotu = input("Numer lotu: ")
    miasto_odlotu = input("Miasto odlotu: ")
    miasto_przylotu = input("Miasto przylotu: ")

    while True:
        try:
            data_odlotu = datetime.strptime(input("Data odlotu (w formacie dd/mm/rrrr) "),'%d/%m/%Y').date()
            break
        except ValueError:
            print("Błąd: Format daty jest nieprawidłowy. Spróbuj ponownie.")

    while True:
        try:
            godzina_odlotu = datetime.strptime(input("Godzina odlotu (w formacie HH:MM):  "),'%H:%M').time()
            break
        except ValueError:
            print("Błąd: Format godziny jest nieprawidłowy. Spróbuj ponownie.")


    data_i_godzina_odlotu = datetime.combine(data_odlotu, godzina_odlotu)

    while True:
        try:
            czas_lotu=int(input("Podaj czas lotu:  (w minutach):  "))
            czas_trwania = timedelta(minutes=czas_lotu)
            break
        except ValueError:
            print("Błąd: Czas lotu został podany nieprawidłowo. Spróbuj ponownie.")


    # Obliczenie daty i godziny przylotu
    data_i_godzina_przylotu = data_i_godzina_odlotu + czas_trwania

    # Pobieramy cenę biletu i dostępne miejsca, konwertując je do odpowiednich typów
    while True:
        try:

            cena_biletu = float(input("Cena biletu (w PLN): "))
            dostepne_miejsca = int(input("Dostępne miejsca: "))
            break
        except ValueError:

            print("Błąd: Cena biletu musi być liczbą (np. 250 lub 100.22), a dostępne miejsca liczbą całkowitą. Spróbuj ponownie.")

###############################################
    #  Tworzymy obiekt Lot z podanymi danymi
    nowy_lot = Lot(numer_lotu, miasto_odlotu, miasto_przylotu, data_i_godzina_odlotu,czas_lotu,data_i_godzina_przylotu,cena_biletu, dostepne_miejsca,dostepne_miejsca)


    os.system('cls')
    nowy_lot.wyswietl_informacje()
    print("--------------------------------------------")
    print("\nNowy lot został utworzony:")
    time.sleep(5)
    os.system('cls')

    from DataRepo import odczytajSlownikZPliku,dodaj_klucz,slownikToFile
#Pobranie zawartości słownika przechowujacego loty
    Loty_Disc = odczytajSlownikZPliku(lot_file)
#Dodanie obiektu do listy i przypisanie pierwszego wolnego klucza
    Loty_Disc = dodaj_klucz(Loty_Disc,nowy_lot)



    Loty_Disc = dict(sorted(Loty_Disc.items()))
    slownikToFile(Loty_Disc,lot_file)

    return Loty_Disc


#Funkcja usuń lot
def UsunLot():
    os.system('cls')
# Pobranie zawartości słownika przechowujacego loty
    from DataRepo import odczytajSlownikZPliku
    Loty_Disc = odczytajSlownikZPliku(lot_file)
#Wyświetlenie wszystkich lotów
    while True:
        try:
            print("""------------------LISTA LOTÓW:------------------

            """)
            for klucz, lot in Loty_Disc.items():
                print(f"Lot o kluczu {klucz}:")
                lot.wyswietl_informacje()
                print("-" * 30)  # Separator dla lepszej czytelności

# Uzytkownik wprowadza klucz lotu którego chce usunąc
            klucz = int(input("Podaj klucz (liczbę), który chcesz usunąć ze słownika: "))

# Sprawdzenie, czy klucz istnieje w słowniku i usuwanie
            if klucz in Loty_Disc:
                del Loty_Disc[klucz]
                os.system('cls')
                print(f"Lot o kluczu {klucz} został usunięty.")
                time.sleep(2)
                os.system('cls')
                from DataRepo import slownikToFile
                slownikToFile(Loty_Disc, lot_file)
                return Loty_Disc
            else:
                print(f"Nie istnieje lot o kluczu:  {klucz} .")
        except ValueError:
            print("Wprowadzono nieprawidłową wartość. Klucz musi być liczbą.")
        os.system('cls')



