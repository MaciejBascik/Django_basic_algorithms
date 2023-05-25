################################
######                    ######
#####   Maciej Baścik 2P   #####
######                    ######
################################
class Babelkowe:
    def babelkowe(arr):
        for i in range(len(arr)):  
            for j in range(0, len(arr) - i - 1):         ## pętla do porównywania elementów tablicy
                if arr[j] > arr[j + 1]:                  ## porównanie ze sobą 2 elementów
                    arr[j], arr[j+1] =arr[j+1], arr[j]   ## zamiana elementów jeśli nie spełniają warunku

