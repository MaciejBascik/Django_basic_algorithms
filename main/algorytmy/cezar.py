################################
#####    Szyfr Cezara      #####
################################
######                    ######
#####   Maciej Baścik 2P   #####
######                    ######
################################

## Ten kod jest implementacją szyfru Cezara, który przesuwa litery w alfabecie o stałą liczbę pozycji.

import string
alphabet = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
class Cezar:
    def deszyfruj(key,message):
        
        decrypted_message = ""

        for c in message:

            if c in alphabet:
                position = alphabet.find(c)
                new_position = (position - key) % 26
                new_character = alphabet[new_position]
                decrypted_message += new_character
            else:
                decrypted_message += c

        return decrypted_message

    def szyfruj(key,message):
        message = message.lower()
        message = message.replace(' ','')
        cypher_text = ""
        for letter in message:
            cypher_text = cypher_text + chr((ord(letter) + key - 97) % 26 + 97)
        return cypher_text

