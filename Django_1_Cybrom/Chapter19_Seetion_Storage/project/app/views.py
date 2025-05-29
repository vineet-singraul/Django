from django.shortcuts import render
from .models import Item
# Create your views here.

def home(request):
    all_items = Item.objects.all()
    return render(request,'home.html',{'data':all_items})

def home1(request):
    if request.method=="POST":
        Item_name = request.POST.get('Item_name')
        Description = request.POST.get('Description')
        Price = request.POST.get('Price')
        Quantity = request.POST.get('Quantity')
        print(Item_name)
        Item.objects.create(item_name=Item_name,item_des=Description,item_price=Price,item_quantity=Quantity)
        all_items = Item.objects.all()
        return render(request,'home.html',{'data':all_items})
    else:
        return render(request,'home.html') 



def addcard(request,pk):
    # print(pk)
    cart = request.session.get('cart',[])
    # print(cart)
    if pk in cart:
        msg = 'Alrady Addeed Data : '
        all_items = Item.objects.all()
        return render(request,'home.html',{'data':all_items})
    else:
        cart.append(pk)
        print(cart)
        msg = 'succesfullt added ....'
        request.session['cart']=cart
        all_items = Item.objects.all()
        return render(request,'home.html',{'data':all_items,'msg':msg})



def showcart(request):
    cart = request.session.get('cart',[])
    print("*************",cart)
    all_data = []
    total_ammount = 0
    for i in cart:
        item = Item.objects.get(id=i)
        total_ammount += (item.item_quantity*item.item_price)
        all_data.append(item)
    return render(request,'cart.html',{'cart':all_data,'ammount':total_ammount})    





def delete(request, pk):
    cart = request.session.get('cart', [])

    if pk in cart:
        cart.remove(pk)
        request.session['cart'] = cart 
        
    all_data = []
    total_amount = 0
    for i in cart:
        item = Item.objects.get(id=i)
        total_amount += item.item_quantity * item.item_price
        all_data.append(item)
    return render(request, 'cart.html', {'cart': all_data, 'ammount': total_amount})