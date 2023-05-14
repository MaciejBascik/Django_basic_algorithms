################################
######                    ######
#####   Maciej Baścik 2P   #####
######                    ######
################################

# Funkcja iteracyjnego wyszukiwania binarnego
# Zwraca indeks elementu x w tablicy arr, jeśli jest obecny,
# w przeciwnym razie zwraca -1
class Binarny:
    def Wyszukaj(data, cel):
        low = 0
        high = len(data) - 1
        mid = 0

        while low <= high:

            mid = (high + low) // 2

            # Jeśli x jest większy, ignoruj lewą połowę

            if data[mid] < cel:
                low = mid + 1

            # Jeśli x jest mniejszy, ignoruj prawą połowę

            elif data[mid] > cel:
                high = mid - 1

            # oznacza, że x jest obecny w środku
            else:
                return mid

        # Jeśli dojdziemy tutaj, to element nie był obecny

        return -1
