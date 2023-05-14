from django import forms

class LuhnaForm(forms.Form):
    number = forms.CharField(label="Podaj numer karty", max_length=None, required=True)
class CezarForm(forms.Form):
    sign = forms.CharField(label="Zakodować czy odkodować (z/o)", max_length=None, required=True)
    text = forms.CharField(label="Wpisz swój tekst", max_length=100,required=True)
    key = forms.CharField(label="Wpisz miejsce przesuniecia alfabetu", max_length=None,required=True)
 
class BinarnyForm(forms.Form):
    data = forms.CharField(label="Podaj liczby po przecinku", max_length=None, required=True)
    cel = forms.CharField(label="Podaj liczbę, którą szukasz", max_length=None,required=True)
class ResztaForm(forms.Form):
    kwota = forms.CharField(label="Podaj kwotę do zapłacenia", max_length=None, required=True)
    kwotaWprowadzona = forms.CharField(label="Podaj kwotę wpłaconą", max_length=None,required=True)
class FrancjaForm(forms.Form):
    arr = forms.CharField(label="Podaj tablice do posortowania", max_length=None, required=True)

class PolskaForm(forms.Form):
    arr = forms.CharField(label="Podaj tablice do posortowania", max_length=None, required=True)


class BabelkoweForm(forms.Form):
    arr = forms.CharField(label="Podaj tablice do posortowania", max_length=None, required=True)
class WyborForm(forms.Form):
    arr = forms.CharField(label="Podaj tablice do posortowania", max_length=None, required=True)
class EuklidesForm(forms.Form):
    a = forms.CharField(label="Podaj liczbe a", max_length=None, required=True)
    b = forms.CharField(label="Podaj liczbe b", max_length=None, required=True)

        
         