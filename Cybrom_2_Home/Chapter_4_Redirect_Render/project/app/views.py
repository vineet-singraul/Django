from django.shortcuts import render,redirect

# Create your views here.


def home(request):
    name , city = 'vineet' , 'Bhopal'
    return redirect(f'/index/?name={name}&city={city}')

def index(request):
    print("Parametre or URL ki Information hold karega",request)
    print("Method ------ > > > : ",request.method)
    print("Data Show Hoga ----> > > : ", request.GET)
    x = request.GET.get('name')
    y = request.GET.get('city')
    print("X Value IS : ",x)
    print("Y Value IS : ",y)
    return render(request , 'index.html' , {'key1':x , 'key2':y})