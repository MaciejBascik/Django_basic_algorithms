################################
#####    Algorytm Luhna    #####
################################
######                    ######
#####   Maciej Baścik 2P   #####
######                    ######
################################

## Program w Pythonie 3 implementujący algorytm Luhna
## Zwraca True, jeśli podany numer karty jest poprawny
### Algorytm służący do sprawdzania poprawności wpisania numeru. Jest on używany m.in. do walidacji numerów kart kredytowych, ciągów liczbowych itd. 
class Luhna:
    def Luhn(cardNo):
        
        nDigits = len(cardNo)
        nSum = 0
        isSecond = False
        
        for i in range(nDigits - 1, -1, -1):
            d = ord(cardNo[i]) - ord('0')
        
            if (isSecond == True):
                d = d * 2
    
            # Dodajemy dwie cyfry, aby obsłużyć przypadki, w których podwajanie 
            # powoduje otrzymanie dwóch cyfr
            nSum += d // 10
            nSum += d % 10
    
            isSecond = not isSecond
        
        if (nSum % 10 == 0):
            return "Podana karta jest poprawna"
        else:
            return "Podana karta jest niepoprawna"
 

