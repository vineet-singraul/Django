from django.shortcuts import render,redirect # type: ignore

# Create your views here.

def home(request):
    name , city = 'vineet' , 'Bhopal'
    return redirect(f'/index/?name={name}&city={city}')



def index(request):
    print("REEEEEEEEEEEEEEEEEEEEE",request.method) 
    print("RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR",request.GET)
    x = request.GET.get('name')
    y = request.GET.get('city')
    print(x , y)
    return render(request ,'index.html',{'key1':x , 'key2':y})