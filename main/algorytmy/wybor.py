################################
######                    ######
#####   Maciej Baścik 2P   #####
######                    ######
################################

# Selekcja przez wybór
class Wybor:
    def selekcja(array, n):
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                # wybranie minimalnego elementu w każdej iteracji
                if array[j] < array[min_index]:
                    min_index = j
            # zamiana elementów w celu posortowania tablicy
            (array[i], array[min_index]) = (array[min_index], array[i])

