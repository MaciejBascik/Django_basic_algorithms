from django.shortcuts import render, redirect
from django.urls import reverse
from .algorytmy.luhna import Luhna
from .algorytmy.cezar import Cezar
from .algorytmy.reszta import Reszta
from .algorytmy.francja import Francja
from .algorytmy.polska import Polska
#from .algorytmy.polska import Polska
from .algorytmy.binarny import Binarny
from .algorytmy.wybor import Wybor
from .algorytmy.euklides import Euklides
from .forms import CezarForm,BinarnyForm,ResztaForm,PolskaForm,FrancjaForm,WyborForm,EuklidesForm,LuhnaForm

def home(request):
    return render(request, 'main/home.html')

def luhnaDate(request):
    if request.method == 'POST':
        form = LuhnaForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['number']
            wynik = Luhna.Luhn(number)
            return redirect(reverse('luhna', kwargs={'wynik': wynik}))
    else:
        form = LuhnaForm()
    return render(request, 'main/luhnaDate.html', {'form': form})

def luhna(request, wynik):
    return render(request, 'main/luhna.html', {'wynik': wynik})


def cezarDate(request):
    if request.method == 'POST':
        form = CezarForm(request.POST)
        if form.is_valid():
            tekst = form.cleaned_data['tekst']
            literka = form.cleaned_data['sign']
            if literka == 'o' or literka == 'O':
                wynik = Cezar.odszyfruj(tekst)
            elif literka == 'z' or literka == 'Z':
                wynik = Cezar.cyfruj(tekst)
            else:
                wynik = 'Podaj literę o lub z'
            return redirect(reverse('cezar', kwargs={'wynik': wynik}))
    else:
        form = CezarForm()
    return render(request, 'main/cezarDate.html', {'form': form})

def cezar(request, wynik):
    return render(request, 'main/cezar.html', {'wynik': wynik})


def binarnyDate(request):
    if request.method == 'POST':
        form = BinarnyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']
            cel = form.cleaned_data['cel']
            cel = int(cel)
            data = data.split(',')
            for i in range(0, len(data)):
                data[i] = int(data[i])
            wynik = Binarny.Wyszukaj(data,cel)     
            if wynik != -1:
                wynikD = f"Element znajduję się na pozycji indeksu {str(wynik)}"
                print(wynikD)
            else:
                wynikD = ("Element nie znajduje się w tablicy")

            return redirect(reverse('binarny', kwargs={'wynik': wynikD}))
    else:
        form = BinarnyForm()
    return render(request, 'main/binarnyDate.html', {'form': form})

def binarny(request, wynik):
    return render(request, 'main/binarny.html', {'wynik': wynik})


def resztaDate(request):
    if request.method == 'POST':
        form = ResztaForm(request.POST)
        if form.is_valid():
            kwota = form.cleaned_data['kwota']
            kwotaWprowadzona = form.cleaned_data['kwotaWprowadzona']
            wynik = Reszta.Wydaj(kwota,kwotaWprowadzona)     
            wynikLista = []
        for nominal, ilosc in wynik.items():
            wynik = ("{} zł x {}".format(nominal, ilosc))
            wynikLista.append(wynik)
        return redirect(reverse('reszta', kwargs={'wynikLista0': wynikLista[0],'wynikLista1': wynikLista[1],'wynikLista2': wynikLista[2],'wynikLista3': wynikLista[3],'wynikLista4': wynikLista[4],'wynikLista5': wynikLista[5]}))
    else:
        form = ResztaForm()
    return render(request, 'main/resztaDate.html', {'form': form})

def reszta(request, wynikLista0,wynikLista1,wynikLista2,wynikLista3,wynikLista4,wynikLista5):
    return render(request, 'main/reszta.html', {'wynikLista0': wynikLista0,'wynikLista1': wynikLista1,'wynikLista2': wynikLista2,'wynikLista3': wynikLista3,'wynikLista4': wynikLista4,'wynikLista5': wynikLista5})

def francjaDate(request):
    if request.method == 'POST':
        form = FrancjaForm(request.POST)
        if form.is_valid():
            lista = form.cleaned_data['arr']
            lista = lista.split(',')    
            for i in range(0, len(lista)):
                lista[i] = int(lista[i])

            Francja.quicksort(lista,0,len(lista) - 1)

        return redirect(reverse('francja', kwargs={'wynik': lista}))
    else:
        form = FrancjaForm()
    return render(request, 'main/francjaDate.html', {'form': form})

def francja(request, wynik):
    return render(request, 'main/francja.html', {'wynik': wynik})

def polskaDate(request):
    if request.method == 'POST':
        form = PolskaForm(request.POST)
        if form.is_valid():
            lista = form.cleaned_data['arr']
            lista = lista.split(',')
            for i in range(0, len(lista)):
                lista[i] = int(lista[i])
            wynik = Polska.polska(lista) 

        return redirect(reverse('polska', kwargs={'wynik': wynik}))
    else:
        form = PolskaForm()
    return render(request, 'main/polskaDate.html', {'form': form})

def polska(request, wynik):
    return render(request, 'main/polska.html', {'wynik': wynik})

def wyborDate(request):


    if request.method == 'POST':
        form = WyborForm(request.POST)
        if form.is_valid():
            lista = form.cleaned_data['arr']
            lista = lista.split(',')
            for i in range(0, len(lista)):
                lista[i] = int(lista[i])
            Wybor.selekcja(lista, len(lista)) 
            wynik = lista
        return redirect(reverse('wybor', kwargs={'wynik': wynik}))
    else:
        form = PolskaForm()
    return render(request, 'main/wyborDate.html', {'form': form})

def wybor(request, wynik):
    return render(request, 'main/wybor.html', {'wynik': wynik})


def euklidesDate(request):
    if request.method == 'POST':
        form = EuklidesForm(request.POST)
        if form.is_valid():
            a = int(form.cleaned_data['a'])
            b = int(form.cleaned_data['b'])
            wynik = Euklides.euklides(a,b) 

        return redirect(reverse('euklides', kwargs={'wynik': wynik}))
    else:
        form = EuklidesForm()
    return render(request, 'main/euklidesDate.html', {'form': form})

def euklides(request, wynik):
    return render(request, 'main/euklides.html', {'wynik': wynik})

def babelkoweDate(request):
    if request.method == 'POST':
        form = PolskaForm(request.POST)
        if form.is_valid():
            lista = form.cleaned_data['arr']
            lista = lista.split(',')
            for i in range(0, len(lista)):
                lista[i] = int(lista[i])
            wynik = Polska.polska(lista) 

        return redirect(reverse('babelkowe', kwargs={'wynik': wynik}))
    else:
        form = PolskaForm()
    return render(request, 'main/babelkoweDate.html', {'form': form})

def babelkowe(request, wynik):
    return render(request, 'main/babelkowe.html', {'wynik': wynik})

