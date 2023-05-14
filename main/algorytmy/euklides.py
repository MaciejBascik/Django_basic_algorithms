################################
######                    ######
#####   Maciej Baścik 2P   #####
######                    ######
################################

class Euklides:
    def euklides(a, b):
        while b != 0:                   # dopóki b nie jest równy 0
            temp = b                    # tymczasowo przypisz wartość b do zmiennej temp
            b = a % b                   # przypisz do b resztę z dzielenia a przez b
            a = temp                    # przypisz do a wartość tymczasowej zmiennej temp
        return a                        # zwróć a, który jest największym wspólnym dzielnikiem a i b

