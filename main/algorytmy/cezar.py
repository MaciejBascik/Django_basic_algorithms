################################
#####    Szyfr Cezara      #####
################################
######                    ######
#####   Maciej Baścik 2P   #####
######                    ######
################################

## Ten kod jest implementacją szyfru Cezara, który przesuwa litery w alfabecie o stałą liczbę pozycji.

import string
alphabet = list(string.ascii_lowercase)


## Definiujemy słownik szyfrujący, który mapuje litery na inne litery w alfabecie
szyfr = {'a': 'c', 'ą': 'ć', 'b': 'd','c' : 'e', 'ć': 'ę','d':'f','e':'g','ę':'h','f': 'i', 'g':'j', 'h':'k', 'i':'l',
'j':'ł','k':'m','l':'n','ł': 'ń', 'm' : 'o', 'n' : 'ó','ń':'p','o':'r','ó': 's','p':'ś','r': 't','s':'u','ś':'w','t':'y',
'u':'z','w':'ź','y':'ż','z':'a','ź':'ą','ż':'b'}
szyfr2 = {'c': 'a', 'ć': 'ą', 'd': 'b','e' : 'c', 'ę': 'ć','f':'d','g':'e','h':'ę','i': 'f', 'j':'g', 'k':'h', 'l':'i',
'ł':'j','m':'k','n':'l','ń': 'ł', 'o' : 'm', 'ó' : 'n','p':'ń','r':'o','s': 'ó','ś':'p','t': 'r','u':'s','w':'ś','y':'t',
'z':'u','ź':'w','ż':'y','a':'z','ą':'ź','b':'ż'}

## Tworzymy dwie puste listy, które będą przechowywać zaszyfrowany i odszyfrowany tekst
lista = []
lista2 = []

    ## Funkcja listToString() konwertuje listę znaków na string
def listToString(s):
        str1 = ""
        for ele in s:
            str1 += ele
        return str1

class Cezar:


    ## Funkcja cyfruj() szyfruje podany tekst zgodnie z szyfrem Cezara
    def cyfruj(txt):
            for i in range(len(txt)):
                if (txt[0 + i] == " "):
                    lista.append(" ")
                else:
                    txt2 = txt.replace(txt[0 + i], szyfr[txt[0 + i]])  
                    lista.append(txt2[0+i])
            return listToString(lista)
    ## Funkcja odszyfruj() odszyfrowuje podany tekst zgodnie z szyfrem Cezara
    def odszyfruj(txt3):
        for i in range(len(txt3)):
            if (txt3[0 + i] == " "):
                lista2.append(" ")
            else:
                txtodszyf = txt3.replace(txt3[0 + i], szyfr2[txt3[0 + i]])
                lista2.append(txtodszyf[0+i])
        return listToString(lista2)



## Wywołujemy funkcję cyfruj() lub odszyfruj() w zależności od wyboru użytkownika




