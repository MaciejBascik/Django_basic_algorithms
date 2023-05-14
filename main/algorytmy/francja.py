################################
######                    ######
#####   Maciej Baścik 2P   #####
######                    ######
################################


class Francja:
    def partition(arr, first, last, start, mid):
        
        pivot = arr[last]
        end = last
        
        # Iteruj, dopóki środek nie będzie większy niż koniec.

        while (mid[0] <= end):
            
            # Zamień pozycję elementu na początku, jeśli jego wartość jest mniejsza niż pivot.
       
            if (arr[mid[0]] < pivot):
                
                arr[mid[0]], arr[start[0]] = arr[start[0]], arr[mid[0]]
                
                mid[0] = mid[0] + 1
                start[0] = start[0] + 1
                
            #  Zamień pozycję elementu na końcu, jeśli jego wartość jest większa niż pivot.

            elif (arr[mid[0]] > pivot):
                
                arr[mid[0]], arr[end] = arr[end], arr[mid[0]]
                
                end = end - 1
                
            else:
                mid[0] = mid[0] + 1

# Funkcja sortująca elementy tablicy w trzech przypadkach
    def quicksort(arr,first,last):
    # Pierwszy przypadek, gdy tablica zawiera tylko 1 element
        if (first >= last):
            return
        
    # Drugi przypadek, gdy tablica zawiera tylko 2 elementy
        if (last == first + 1):
            
            if (arr[first] > arr[last]):
                
                arr[first], arr[last] = arr[last], arr[first]
                
                return

    # Trzeci przypadek, gdy tablica zawiera więcej niż 2 elementy
        start = [first]
        mid = [first]

    # Funkcja do podziału tablicy.
        Francja.partition(arr, first, last, start, mid)
        
# Rekurencyjnie sortuj podlistę zawierającą elementy mniejsze od pivot.
    
        Francja.quicksort(arr, first, start[0] - 1)

# Rekurencyjnie sortuj podlistę zawierającą elementy większe od pivot
   
        Francja.quicksort(arr, mid[0], last)



