################################
#####    Szyfr Cezara      #####
################################
######                    ######
#####   Maciej Baścik 2P   #####
######                    ######
################################

## Ten kod jest implementacją szyfru Cezara, który przesuwa litery w alfabecie o stałą liczbę pozycji.

import string #Importuje moduł string, który zawiera funkcje do manipulacji tekstowymi operacjami, takie jak operacje na ciągach znaków.
alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz" Tworzy zmienną "alphabet" przechowującą małe litery alfabetu.
class Cezar: #Definiuje klasę "Cezar", która zawiera dwie metody - "deszyfruj" i "szyfruj".

    def deszyfruj(key,message): #Metoda "deszyfruj" przyjmuje dwa argumenty - "key" (klucz) i "message" (wiadomość do zdeszyfrowania).


        # Iteruje przez każdy znak w wiadomości "message". 



        decrypted_message = ""
        for c in message:
        # Jeśli znak znajduje się w alfabecie, oblicza nową pozycję litery po przesunięciu o "key" pozycji w lewo modulo 26 (liczba liter w alfabecie). 
            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position - key) % 26
                new_character = alphabet[new_position]        
                # Następnie dodaje zaszyfrowaną literę do zdeszyfrowanej wiadomości "decrypted_message". 
                decrypted_message += new_character
            else:        
                # Jeśli znak nie znajduje się w alfabecie, dodaje go bez zmian.
                decrypted_message += c

        return decrypted_message #Zwraca zdeszyfrowaną wiadomość.

    def szyfruj(key,message): #Metoda "szyfruj" przyjmuje dwa argumenty - "key" (klucz) i "message" (wiadomość do zaszyfrowania).
        message = message.lower() #Przekształca wiadomość na małe litery.
        message = message.replace(' ','') #Usuwa spacje z wiadomości.
        # Iteruje przez każdą literę w przekształconej wiadomości. 
        cypher_text = ""
        for letter in message:
            # Wykorzystuje funkcję chr() i ord() do przesunięcia litery o "key" pozycji w prawo (względem małych liter alfabetu) i obliczenia nowej zaszyfrowanej litery. 
            # Dodaje zaszyfrowaną literę do zaszyfrowanej wiadomości "cypher_text".
            cypher_text = cypher_text + chr((ord(letter) + key - 97) % 26 + 97)
        return cypher_text #Zwraca zaszyfrowaną wiadomość.

