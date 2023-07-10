from django.shortcuts import render,redirect
from .algorytmy.luhna import Luhna
from .algorytmy.cezar import Cezar
from .algorytmy.reszta import Reszta
from .algorytmy.francja import Francja
from .algorytmy.polska import Polska
#from .algorytmy.polska import Polska
from .algorytmy.binarny import Binarny
from .algorytmy.wybor import Wybor
from .algorytmy.euklides import Euklides
from .algorytmy.Bubble import Bubble
from django.contrib.auth.models import User
from users import views


def home(request):
    if not request.user.is_authenticated:
        return redirect(views.loginView)
    return render(request, 'main/home.html',{"username":request.user})

def luhna(request):
    if not request.user.is_authenticated:
        return redirect(views.loginView)
    if request.method == 'POST':
            number = request.POST.get('number')
            result = Luhna.Luhn(number)
            return render(request,'main/luhna.html', {'result': result})
    return render(request, 'main/luhna.html', {"username":request.user})


def cezar(request):
    if not request.user.is_authenticated:
        return redirect(views.loginView)
    if request.method == 'POST':
            text = request.POST.get('text')
            key = int(request.POST.get('key'))
            sign = request.POST.get('sign')
            if sign.upper() == 'O':
                result = Cezar.deszyfruj(key, text)
                return render(request,'main/cezar.html', {'result': result})
            elif sign.upper() == 'Z':
                result = Cezar.szyfruj(key, text)
                return render(request,'main/cezar.html', {'result': result})
            else:
                result = 'Podaj literę o lub z'
                return render('main/cezar.html', {'result': result})
    return render(request, 'main/cezar.html', {"username":request.user})



def binarny(request):
    if not request.user.is_authenticated:
        return redirect(views.loginView)
    if request.method == 'POST':
            data = request.POST.get('data')
            key =  int(request.POST.get('key'))
            data = data.split(',')
            for i in range(0, len(data)):
                data[i] = int(data[i])
            result = Binarny.Wyszukaj(data,key)
            if result != -1:
                resultText = f"Element is on index position {str(result)}"
            else:
                resultText = ("Element isn't in array")
            return render(request,'main/binarny.html', {'result': resultText})
   
    return render(request,'main/binarny.html',{"username":request.user})


def reszta(request):
    if not request.user.is_authenticated:
        return redirect(views.loginView)
    if request.method == 'POST':
            price = int(request.POST.get('price'))
            pricePaid = int(request.POST.get('pricePaid'))
            result = Reszta.Wydaj(price,pricePaid)     
            ResultArray = []
            for nominal, ilosc in result.items():
                result = ("{} zł x {}".format(nominal, ilosc))
                ResultArray.append(result)
            print(ResultArray[0])
            return render(request,'main/reszta.html', {'wynikLista0': ResultArray[0],'wynikLista1': ResultArray[1],'wynikLista2': ResultArray[2],'wynikLista3': ResultArray[3],'wynikLista4': ResultArray[4],'wynikLista5': ResultArray[5]})
    return render(request, 'main/reszta.html', {"username":request.user})


def francja(request):
    if not request.user.is_authenticated:
        return redirect(views.loginView)
    if request.method == 'POST':
            arr = request.POST.get('arr')
            arr = arr.split(',')
            for i in range(0, len(arr)):
                arr[i] = int(arr[i])

            Francja.quicksort(arr,0,len(arr) - 1)

            return render(request,'main/francja.html',{'result': arr})
    return render(request, 'main/francja.html', {"username":request.user})



def polska(request):
    if not request.user.is_authenticated:
        return redirect(views.loginView)
    if request.method == 'POST':
            arr = request.POST.get('arr')
            arr = arr.split(',')
            for i in range(0, len(arr)):
                arr[i] = int(arr[i])
            result = Polska.polska(arr) 

            return render(request, 'main/polska.html', {'result': result})
    return render(request, 'main/polska.html', {"username":request.user})


def wybor(request):
    if not request.user.is_authenticated:
        return redirect(views.loginView)
    if request.method == 'POST':
            arr = request.POST.get('arr')
            arr = arr.split(',')
            for i in range(0, len(arr)):
                arr[i] = int(arr[i])
            Wybor.selekcja(arr, len(arr)) 
            result = arr
            return render(request, 'main/wybor.html', {'result': result})
    return render(request, 'main/wybor.html', {"username":request.user})





def euklides(request):
    if not request.user.is_authenticated:
        return redirect(views.loginView)
    if request.method == 'POST':
            numberOne = int(request.POST.get('one'))
            numberTwo = int(request.POST.get('two'))
            result = Euklides.euklides(numberOne,numberTwo) 

            return render(request, 'main/euklides.html', {'result': result})
    return render(request, 'main/euklides.html', {"username":request.user})





def babelkowe(request):
    if not request.user.is_authenticated:
        return redirect(views.loginView)
    if request.method == 'POST':
            arr = request.POST.get('arr')
            arr = arr.split(',')
            print(arr)
            for i in range(0, len(arr)):
                    arr[i] = int(arr[i])
            Bubble.Bubble(arr) 
            result = arr

            return render(request,'main/babelkowe.html', {'result': result})
    return render(request, 'main/babelkowe.html', {"username":request.user})



