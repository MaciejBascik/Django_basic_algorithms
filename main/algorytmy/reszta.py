################################
######                    ######
#####   Maciej Baścik 2P   #####
######                    ######
################################

class Reszta:
    try:
        # Wprowadzamy dane 
        # Metoda sprawdzenia ilosci monet
        def Wydaj(kwota, platnosc):
            nominaly = [50, 20, 10, 5, 2, 1]
            kwota, platnosc = int(kwota), int(platnosc)
            reszta = platnosc - kwota
            wydane_nominaly = {}
            for nominal in nominaly:
                if reszta >= nominal: 
                    ilosc = int(reszta // nominal)  # zamieniamy na całkowite liczby
                    wydane_nominaly[nominal] = ilosc
                    reszta -= ilosc * nominal
                else:
                    wydane_nominaly[nominal] = 0
            return wydane_nominaly

        


            
    except ValueError:     
        print("Wpisz liczbę!")
    except TypeError:
        print("Wpisz liczbę!") 
    except NameError:   
        print("")
