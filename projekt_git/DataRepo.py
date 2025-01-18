import  os,json

pasazer_file = "pasazer.json"
lot_file = "lot.json"
rezerwacja_file = "rezerwacja.json"
lista_plikow = [pasazer_file,lot_file,rezerwacja_file]


# Funkcja do zapisywania danych z pliku do słownika (klucz -> obiekt)

def odczytajSlownikZPliku(nazwaPliku):

# Jeśli plik nie istnieje to go tworzy i daje pusty slownik
    if not os.path.exists(nazwaPliku):
        with open(nazwaPliku, "x") as f:
# Tworzymy pusty plik JSON
            json.dump({}, f)
        Slownik={}
        return Slownik

#dla lotu
    if(nazwaPliku==lot_file):
        from datetime import datetime
        from loty import Lot
        with open(lot_file, "r") as f:
                    if os.path.getsize(lot_file) > 0:
                        try: 
                            dane = json.load(f)
                            loty = {
                                int(k): Lot(
                                    numer_lotu=v["numer_lotu"],
                                    miasto_odlotu=v["miasto_odlotu"],
                                    miasto_przylotu=v["miasto_przylotu"],
                                    data_i_godzina_odlotu=datetime.fromisoformat(v["data_i_godzina_odlotu"]),
                                    czas_lotu=int(v["czas_lotu"]),
                                    data_i_godzina_przylotu=datetime.fromisoformat(v["data_i_godzina_przylotu"]),
                                    cena_biletu=v["cena_biletu"],
                                    dostepne_miejsca=v["dostepne_miejsca"],
                                    wolne_miejsca=v["wolne_miejsca"]
                                )
                                for k, v in dane.items()
                            }
                        except json.JSONDecodeError:
                            loty = {}
                    else:
                        loty={}

                    return loty
######################################

#dla pasazera
    elif(nazwaPliku==pasazer_file):

        from pasazer import Pasazer
        with open(pasazer_file, 'r') as f:
            if os.path.getsize(pasazer_file) > 0:
                try:
                    json_data = json.load(f)
                    pasazerowie  = {
                        int(k): Pasazer.from_dict(v) for k, v in json_data.items()
                    }
                except json.JSONDecodeError:
                    pasazerowie = {}
            else:
                pasazerowie = {}

            return pasazerowie

######################################
#dla rezerwacja

    elif(nazwaPliku==rezerwacja_file):

            from rezerwacje import Rezerwacja
            with open(rezerwacja_file, 'r') as f:
                if os.path.getsize(rezerwacja_file) > 0:
                    try:
                        json_data = json.load(f)
                        rezerwacjeLotow  = {
                            int(k): Rezerwacja.from_dict(v) for k, v in json_data.items()
                        }
                    except json.JSONDecodeError:
                        rezerwacjeLotow = {}
                else:
                    rezerwacjeLotow = {}

                return rezerwacjeLotow

    elif(nazwaPliku==rezerwacja_file):

        rezerwacja = {}
        return rezerwacja
    else:
        "wystapił jakis blad"



# Funkcja przypisuje pierwszy wolny klucz w slowniku i przypisuja ją jako klucz do nowo-dodanego obiektu

def dodaj_klucz(slownik,obiekt):
    # Znajdź najbliższy wolny klucz zaczynając od 1
    klucz = 1
    while klucz in slownik:
        klucz += 1
    # Dodaj lot do słownika z tym kluczem
    slownik[klucz] = obiekt

    return slownik

# Funkcja zapis słownika do pliku JSON

def slownikToFile(slownik,fileName):

    dane_json = {str(key): x.to_dict() for key, x in slownik.items()}

    # Zapis do pliku JSON
    with open(fileName, "w", encoding="utf-8") as file:
        json.dump(dane_json, file, ensure_ascii=False, indent=4)



