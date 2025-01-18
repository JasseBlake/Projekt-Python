import os,time
from datetime import datetime

pasazer_file = "pasazer.json"



class Pasazer:
# Konstruktor klasy Pasazer
    def __init__(self, imie, nazwisko, data_urodzenia):
        self.imie = imie
        self.nazwisko = nazwisko
        self.data_urodzenia = data_urodzenia

# Metoda konwertująca obiekt typu Pasazer na słownik
    def to_dict(self):
        return {
            "imie": self.imie,
            "nazwisko": self.nazwisko,
            "data_urodzenia": self.data_urodzenia.isoformat(),
        }

# Metoda wyświetlająca informacje o pasazerze
    def wyswietl_informacjePas(self):
        print(f"Imię: {self.imie}")
        print(f"Nazwisko: {self.nazwisko}")
        print(f"data_urodzenia: {self.data_urodzenia}")

# Zmienia slównik na obiekt typu Pasazer - uzywane przy wczytywanii z pliku JSON
    @staticmethod
    def from_dict(data):
        return Pasazer(
            imie=data["imie"],
            nazwisko=data["nazwisko"],
            data_urodzenia=datetime.fromisoformat(data["data_urodzenia"]).date())


# Funkcja Dodaj Pasazera
def DodajPasazer():


    imie = input("Podaj imię : ")
    nazwisko = input("Podaj nazwisko: ")
    while True:
        try:
            data_urodzenia = datetime.strptime(input("Data urodzenia (w formacie dd/mm/rrrr) "),'%d/%m/%Y').date()

# Sprawdzenie, czy data urodzenia nie jest z przyszłości
            if data_urodzenia > datetime.now().date():
                print("Błąd: Data urodzenia nie może być z przyszłości. Spróbuj ponownie.")
                continue
            break
        except ValueError:
            print("Błąd: Format daty jest nieprawidłowy. Spróbuj ponownie.")


###############################################
# Tworzymy obiekt pasazer z podanymi danymi
    nowy_pasazer = Pasazer(imie,nazwisko,data_urodzenia)
    print("--------------------------------------------")
    print("\nNowy pasazer został utworzony")
# Wyświtlanie danych utworzonego pasazera
    nowy_pasazer.wyswietl_informacjePas()

    time.sleep(5)
    os.system('cls')

    from DataRepo import odczytajSlownikZPliku,dodaj_klucz,slownikToFile
# Pobieranie aktualnych danych do słwonika z pliku JSON
    Pasazer_Disc = odczytajSlownikZPliku(pasazer_file)

# Dodanie obiektu do slwonika wraz z pierwszym wolnym kluczem
    Pasazer_Disc = dodaj_klucz(Pasazer_Disc,nowy_pasazer)
    Pasazer_Disc = dict(sorted(Pasazer_Disc.items()))
    slownikToFile(Pasazer_Disc,pasazer_file)
    return Pasazer_Disc



# Funkcja Usuń pasazera
def UsunPasazer():
    os.system('cls')

# Pobieranie aktualnych danych do słwonika z pliku JSON
    from DataRepo import odczytajSlownikZPliku
    Pasazer_Disc = odczytajSlownikZPliku(pasazer_file)

    while True:
        try:
            print("""------------------LISTA PASAZERÓW:------------------

            """)
# Wyświetlenie wszsytkich dostepnych pasazerow wraz z ich inoframcjami
            for klucz, pasazer in Pasazer_Disc.items():
                print(f"Pasazer o kluczu {klucz}:")
                pasazer.wyswietl_informacjePas()
                print("-" * 30)

# Zapytanie o  klucz pasazera ktorego chcemy usunac

            klucz = int(input("Podaj klucz (liczbę), który chcesz usunąć ze słownika: "))

# Sprawdzenie, czy klucz istnieje w słowniku
            if klucz in Pasazer_Disc:
    # Tak - usuwa pasazera i zapisuje dane do pliku JSON i zwraca słownik z aktualnymi danymi
                del Pasazer_Disc[klucz]
                print(f"Pasazer o kluczu {klucz} został usunięty.")
                from DataRepo import slownikToFile
                slownikToFile(Pasazer_Disc, pasazer_file)
                return Pasazer_Disc
            else:
                print(f"Nie istnieje lot o kluczu:  {klucz} .")
        except ValueError:
            print("Wprowadzono nieprawidłową wartość. Klucz musi być liczbą.")

        # Wyczyść konsolę
        os.system('cls')
#


