from django import forms


class ResztaForm(forms.Form):
    kwota = forms.CharField(label="Podaj kwotę do zapłacenia", max_length=None, required=True)
    kwotaWprowadzona = forms.CharField(label="Podaj kwotę wpłaconą", max_length=None,required=True)
class FrancjaForm(forms.Form):
    arr = forms.CharField(label="Podaj tablice do posortowania", max_length=None, required=True)

class PolskaForm(forms.Form):
    arr = forms.CharField(label="Podaj tablice do posortowania", max_length=None, required=True)




class WyborForm(forms.Form):
    arr = forms.CharField(label="Podaj tablice do posortowania", max_length=None, required=True)
class EuklidesForm(forms.Form):
    a = forms.CharField(label="Podaj liczbe a", max_length=None, required=True)
    b = forms.CharField(label="Podaj liczbe b", max_length=None, required=True)

        
         