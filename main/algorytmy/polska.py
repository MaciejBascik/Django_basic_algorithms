
################################
######                    ######
#####   Maciej Baścik 2P   #####
######                    ######
################################


class Polska:
    def polska(arr):
        white = -1
        red = len(arr)# Określenie zmiennych liczby pierwszej i ostatniej w tablicy( odpowiednio high i low )
        while red - white > 1: # jeśli pierwsza liczba w tablicy jest mniejsza od ostastniej to zakończ ( chodzi o zakończeniu cyklu jeśli cała lista została oddana pod sortowanie)
            if arr[white+1] % 2 ==0: # Warunek, jeśli liczba pierwsza jest większa lub równa 10
                white += 1  # to zamień liczbę pierwszą z ostatnią
            else:
                red -= 1 # jeśli warunek nie jest spełniony, to przybieramy kolejną pozycję na liście (od pierwszej liczby)
                arr[white+1],arr[red] = arr[red],arr[white+1]
                 
        return arr # zwracamy posortowaną listę

    

