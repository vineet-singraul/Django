from django.shortcuts import render,redirect
from .models import Customer,Query,DynamicCards
from django.db.models import Q
# Create your views here.


def home(request):
    productDetails = DynamicCards.objects.all()
    onlyImage1 = DynamicCards.objects.filter(db_product_catagurays='men').values_list('db_product_image1', flat=True)
    return render(request, "home.html",{'productDetails':productDetails,'onlyImage1':onlyImage1})

def mens(request):
    productDetails = DynamicCards.objects.filter(db_product_catagurays='men')
    return render(request,"mens.html",{'productDetails':productDetails})

def womens(request):
    productDetails = DynamicCards.objects.filter(db_product_catagurays='women')
    return render(request,"womens.html",{'productDetails':productDetails})

def kides(request):
    productDetails = DynamicCards.objects.filter(db_product_catagurays='kids')
    return render(request,"kides.html",{'productDetails':productDetails})

def electranics(request):
    productDetails = DynamicCards.objects.filter(db_product_catagurays='electronics')
    return render(request,"electranics.html",{'productDetails':productDetails})

def grousary(request):
    return render(request,"grousary.html")


# LOGIN AND SIGNUP KE LIYE
def signup(request):
  if request.method == 'POST':  
    name = request.POST.get('name')
    email = request.POST.get('email')
    password = request.POST.get('password')
    cpaas = request.POST.get('cpaas')
    userImage = request.FILES.get('userImage')
    phoneNumber = request.POST.get('phoneNumber')
    city = request.POST.get('city')
     
    user = Customer.objects.filter(cus_email = email)
    if user.exists():
        userdata = {
        'name': name,
        'email': email,
        'password': password,
        'cpaas': cpaas,
        'phoneNumber': phoneNumber,
        'city': city
      }
        msg = 'Email already exists'
        return render(request, "signup.html", {'msg': msg, 'userdata': userdata})

    else:
        if password == cpaas :
            Customer.objects.create(
              cus_name = name,
              cus_email = email,
              cus_password = password,
              cus_cpassword = cpaas,
              cus_image = userImage,
              cus_phone = phoneNumber,
              cus_location = city
            ) 
            msg = 'Account Successfully created'
            return render(request,"login.html",{'msg':msg})
        else:
             userdata = {
               'name': name,
               'email': email,
               'phoneNumber': phoneNumber,
               'city': city
              }
             msg = 'Password Is Not Match'
             return render(request,"signup.html",{'msg':msg,'userdata':userdata})
  else:
      return render(request,"signup.html")  
  
def login(request):
    ademail = 'admin@gmail.com'
    adpass = 'admin@123'
    id = 0 
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = Customer.objects.filter(cus_email = email)

        if ademail==email and adpass==password:
           request.session['admin_id'] = id  # id = 0
           return redirect('/adminDeshbord/')
            # return redirect(f'/adminDeshbord/?id={id}')
       
        if user.exists():
            userdata = Customer.objects.get(cus_email = email)
            sto_pass = userdata.cus_password

            if password == sto_pass:
                request.session['userdata_id'] = userdata.id   #  Session me id Store ker rahe hai 
                msg = 'password is correct'
                return render(request,"deshbord.html",{'msg':msg,'userdata':userdata})

            else:
                msg = 'password is not match'
                return render(request,"login.html",{'msg':msg,'userdata':userdata})

        else :
            msg = 'email not found create account'
            return render(request,"signup.html",{'msg':msg})
        
    else:
        return render(request,"login.html")
    

# Add TO Cart Ke Liye Hai Functionallity Session Se Data Utha rahe hai  :
def addcard(request, pk, jk):
    cart = request.session.get('cart', [])
    if pk not in cart:
        cart.append(pk)
        request.session['cart'] = cart
        msg = 'Item added'
    else:
        msg = 'Already Added item'
    userdata = Customer.objects.get(id=jk)
    all_item = DynamicCards.objects.all()
    return render(request, 'addToCart.html', {'all_item':all_item,'msg': msg,'userdata':userdata})


# Jab user card iconme click karen to function run hoga
def showCart(request, pk):
    cart = request.session.get('cart', [])  # Session bana rahe hai
    all_Add_Items = []
    total_ammount = 0
    total_item = 0
    total_discount = 0
    total_platformFee = 0
    total_Delivery_Charges = 0
    total_First_amount = 0

    for i in cart:
        # Check ker raha hai ki art ki id se item nikal raha hai
        all_item = DynamicCards.objects.get(id=i)
        all_Add_Items.append(all_item)     # item add ker raha hai list me
        total_item += 1   # total item nikal rahe hai
        total_First_amount += all_item.db_product_real_price  # Real ammount nikal rahe hai
        total_ammount += all_item.db_product_real_price   # real price nikal rahe hai
        total_discount += all_item.db_product_previous_price - all_item.db_product_real_price   # dicount calculate ker rahe hai
        total_platformFee += 0.5   # plate form fee include ker rahe hai
    total_ammount = total_ammount - total_discount + total_platformFee  # total ammount sub kuch - + karne ke baad
    if total_ammount < 2000:
        total_Delivery_Charges = 50
        total_ammount += total_Delivery_Charges
    else:
        total_Delivery_Charges = 0
    total_save_ammount = total_First_amount - total_discount
    userdata = Customer.objects.get(id=pk)

    return render(request, 'addToCart.html', {
        'all_Add_Items': all_Add_Items,
        'userdata': userdata,
        'total_First_amount':total_First_amount,
        'total_item':total_item,
        'total_discount':total_discount,
        'total_ammount':total_ammount,
        'total_platformFee': int(total_platformFee),
        'total_Delivery_Charges':total_Delivery_Charges,
        'total_save_ammount':total_save_ammount
    })

# Cart page se jab user Card Delete karen tab
def cardDelete(request, pk, jk):
    cart = request.session.get('cart', [])

    if pk in cart:
        cart.remove(pk)
        request.session['cart'] = cart

    all_Add_Items = []
    total_ammount = 0
    total_item = 0
    total_discount = 0
    total_platformFee = 0
    total_Delivery_Charges = 0
    total_First_amount = 0

    for i in cart:
        try:
            item = DynamicCards.objects.get(id=i)
            all_Add_Items.append(item)
            total_item += 1
            total_First_amount += item.db_product_previous_price
            total_ammount += item.db_product_real_price
            total_discount += item.db_product_previous_price - item.db_product_real_price
            total_platformFee += 0.5
        except DynamicCards.DoesNotExist:
            continue  # Skip if item was deleted from DB

    total_ammount = total_ammount - total_discount + total_platformFee

    if total_ammount < 2000:
        total_Delivery_Charges = 50
        total_ammount += total_Delivery_Charges

    total_save_ammount = total_First_amount - total_discount

    try:
        userdata = Customer.objects.get(id=jk)
    except Customer.DoesNotExist:
        userdata = None

    return render(request, 'addToCart.html', {
        'all_Add_Items': all_Add_Items,
        'userdata': userdata,
        'total_First_amount': total_First_amount,
        'total_item': total_item,
        'total_discount': total_discount,
        'total_ammount': total_ammount,
        'total_platformFee': int(total_platformFee),
        'total_Delivery_Charges': total_Delivery_Charges,
        'total_save_ammount': total_save_ammount
    })

# Show Product detail jab user image me click karen
def showIDdetails(request, pk, jk):
    userdata = Customer.objects.get(id=jk)
    cardDetail = DynamicCards.objects.get(id=pk)
    discount = cardDetail.db_product_previous_price - cardDetail.db_product_real_price
    return render(request, 'showIDdetails.html', {'cardDetail': cardDetail, 'discount': discount,'userdata':userdata})

# User Ke Payement Page Ke Liye : 
def goForPayment(request,pk,cd):
    userdata = Customer.objects.get(id=pk)
    cardData = DynamicCards.objects.get(id=cd)
    return render(request,'goForPayment.html',{'userdata':userdata,'cardData':cardData})

# Jab User Login Ho
def home1(request, pk):
    userdata = Customer.objects.get(id=pk)
    productDetails = DynamicCards.objects.all()
    onlyImage1 = DynamicCards.objects.filter(db_product_catagurays='men').values_list('db_product_image1', flat=True)
    return render(request, 'home.html', {'userdata': userdata,'productDetails': productDetails,'onlyImage1': onlyImage1})

def mens1(request,pk):
    userdata = Customer.objects.get(id=pk)
    productDetails = DynamicCards.objects.filter(db_product_catagurays='men')
    return render(request,'mens.html',{'userdata':userdata,'productDetails':productDetails})

def womens1(request,pk):
    userdata = Customer.objects.get(id=pk)
    productDetails = DynamicCards.objects.filter(db_product_catagurays='women')
    return render(request,'womens.html',{'userdata':userdata,'productDetails':productDetails})

def kides1(request,pk):
    userdata = Customer.objects.get(id=pk)
    productDetails = DynamicCards.objects.filter(db_product_catagurays='kids')
    return render(request,'kides.html',{'userdata':userdata,'productDetails':productDetails})

def electranics1(request,pk):
    userdata = Customer.objects.get(id=pk)
    productDetails = DynamicCards.objects.filter(db_product_catagurays='electronics')
    return render(request,'electranics.html',{'userdata':userdata,'productDetails':productDetails})

def grousary1(request,pk):
    userdata = Customer.objects.get(id=pk)
    productDetails = DynamicCards.objects.filter(db_product_catagurays='electronicsids')
    return render(request,'grousary.html',{'userdata':userdata,'productDetails':productDetails})




# User Desh Bord Me Perform 
def deshbord(request, pk):
    try:
        userdata = Customer.objects.get(id=pk)
    except Customer.DoesNotExist:
        return redirect('login')  # Redirect to login if user does not exist

    return render(request, "deshbord.html", {'userdata': userdata})

# user ke Desh bord me Query ke liye functions
def query(request, pk):
    user = Customer.objects.get(id=pk)
    userdata = {
        "id": user.id,
        "cus_name": user.cus_name,
        "cus_email": user.cus_email,
        "cus_email": user.cus_email,
        "cus_image": user.cus_image,
        "cus_phone": user.cus_phone,
    }
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('query')
        Query.objects.create(
            cus_name_q=name,
            cus_email_q=email,
            cus_query_q=query
        )
        querydetail = Query.objects.filter(cus_email_q=email)
        return render(request, 'deshbord.html', {'userdata': userdata, 'querydetail': querydetail})
    else:
        return render(request, 'deshbord.html', {'userdata': userdata, 'query': userdata})

def allquery(request,pk):
    print(pk)
    userdata = Customer.objects.get(id=pk)
    print(userdata.cus_email)
    x= userdata.cus_email
    userdata={
        "id":userdata.id,
        "cus_name": userdata.cus_name,
        "cus_email": userdata.cus_email,
        "cus_email": userdata.cus_email,
        "cus_image": userdata.cus_image,
        "cus_phone": userdata.cus_phone,
    }
    querydetail = Query.objects.filter(cus_email_q=x)
    return render(request,'deshbord.html',{'userdata':userdata,'querydetail':querydetail})

def edit(request,pk):
    editdata = Query.objects.get(id=pk)
    email = editdata.cus_email_q   # yaha query model se email nikal rahe hai
    userdata = Customer.objects.get(cus_email=email)
    return render(request,'deshbord.html',{'userdata':userdata , 'editdata':editdata})
    
def quaryupdate(request,pk):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        query = request.POST.get('query')
        print("..............")
        old_query = Query.objects.get(id=pk)
        print("..............",old_query)
        old_query.cus_name_q = name
        old_query.cus_email_q = email
        old_query.cus_query_q = query
        old_query.save()
        allquery = Query.objects.filter(cus_email_q=email)
        userdata = Customer.objects.get(cus_email=email)
        return render(request,'deshbord.html',{'userdata':userdata,'allquery':allquery})
    
def delete(request,pk):
    deletedata = Query.objects.get(id=pk)
    email = deletedata.cus_email_q
    deletedata.delete()
    allquery = Query.objects.filter(cus_email_q=email)
    userdata = Customer.objects.get(cus_email=email)
    return render(request,'deshbord.html',{'allquery':allquery,'userdata':userdata})

def search(request, pk):
    userdata = Customer.objects.get(id=pk)
    if request.method == "POST":
        searchData = request.POST.get('search')
        all_data = Query.objects.filter(
            Q(cus_name_q__icontains=searchData) |
            Q(cus_email_q__icontains=searchData) |
            Q(cus_query_q__icontains=searchData)
        )
        return render(request, 'deshbord.html', {'userdata': userdata, 'all_data': all_data,'searchData':searchData})
    return render(request, 'deshbord.html', {'userdata': userdata, 'querydetail': Query.objects.all()})

#  user ke Deshbord me offer ke liye 
def offer(request, pk):
    userdata = Customer.objects.get(id=pk)
    return render(request, 'deshbord.html', {
        'userdata': userdata,
        'offer': True
    })









# Admin ke Deh Bord ke liye 
def adminDeshbord(request):
    # sk = request.GET   # admin ki id la raha hai url se
    # id = sk.get('id')
    # print("Id xxxxxxxxxx HAI BHAI L : ",id)
    id = request.session.get('admin_id')    # Admin Ki id session me set ker rahe hai
    msg = ""
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        description_section_2 = request.POST.get('description_section_2')
        previous_price = request.POST.get('previous_price')
        offer_percentage = request.POST.get('offer_percentage')
        product_catagurays = request.POST.get('db_product_catagurays')
        real_price = request.POST.get('real_price')
        image1 = request.FILES.get('image1')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        image4 = request.FILES.get('image4')
        image5 = request.FILES.get('image5')
        image6 = request.FILES.get('image6')

        if product_catagurays:
            DynamicCards.objects.create(
                db_product_name=product_name,
                db_product_discription=product_description,
                db_product_discription2=description_section_2,
                db_product_previous_price=previous_price,
                db_product_offer_percentage=offer_percentage,
                db_product_real_price=real_price,
                db_product_catagurays=product_catagurays,
                db_product_image1=image1,
                db_product_image2=image2,
                db_product_image3=image3,
                db_product_image4=image4,
                db_product_image5=image5,
                db_product_image6=image6,
            )
            msg = 'Data Inserted Successfully'
        else:
            msg = 'Category not selected. Data not inserted.'
    return render(request, "adminDeshbord.html", {'msg': msg,'id':id})

# Admin Me Data Tale ke liye:
def allAdminData(request):
    productDetails = DynamicCards.objects.all()
    id = request.session.get('admin_id')  # ✅ Get kar rahe ho session se
    return render(request, "allAdminData.html",{'productDetails':productDetails,'id':id})

# admin ke liye home  functions
def homead(request):
    productDetails = DynamicCards.objects.all()
    id = request.session.get('admin_id')  # ✅ Get kar rahe ho session se
   # Admin Ke Liye Hai Ye : 
    return render(request, "home.html",{'productDetails':productDetails,'id':id})

def mensad(request):
    productDetails = DynamicCards.objects.all()
    id = request.session.get('admin_id')  # ✅ Get kar rahe ho session se
    return render(request, "mens.html",{'productDetails':productDetails,'id':id})

def womensad(request):
    productDetails = DynamicCards.objects.all()
    id = request.session.get('admin_id')  # ✅ Get kar rahe ho session se
    return render(request, "womens.html",{'productDetails':productDetails,'id':id})

def kidesad(request):
    productDetails = DynamicCards.objects.all()
    id = request.session.get('admin_id')  # ✅ Get kar rahe ho session se
    return render(request, "kides.html",{'productDetails':productDetails,'id':id})

def electanicad(request):
    productDetails = DynamicCards.objects.all()
    id = request.session.get('admin_id')  # ✅ Get kar rahe ho session se
    return render(request, "electranics.html",{'productDetails':productDetails,'id':id})

def adminCardDelete(request,prodid):
   cart = DynamicCards.objects.get(id=prodid)
   cart.delete()
   productDetails = DynamicCards.objects.all()
   id = request.session.get('admin_id')
   return render(request, "allAdminData.html",{'productDetails':productDetails,'id':id} ) 

def adminCardEditRead(request,prodid):
    cart = DynamicCards.objects.get(id=prodid)
    id = request.session.get('admin_id')
    return render(request, "adminDeshbord.html",{'id':id,'cart':cart} ) 

def adminConfirmEditData(request, prodIdEdit):
    id = request.session.get('admin_id')
    
    if request.method == 'POST':
        product_name = request.POST.get('product_name')
        product_description = request.POST.get('product_description')
        description_section_2 = request.POST.get('description_section_2')
        previous_price = request.POST.get('previous_price')
        offer_percentage = request.POST.get('offer_percentage')
        product_catagurays = request.POST.get('db_product_catagurays')
        real_price = request.POST.get('real_price')
        image1 = request.FILES.get('image1')

        # Get existing product entry safely
        oldData = DynamicCards.objects.get(id=prodIdEdit)
        # oldData = get_object_or_404(DynamicCards, id=prodIdEdit)

        # Update fields
        oldData.db_product_name = product_name
        oldData.db_product_catagurays = product_catagurays
        oldData.db_product_discription = product_description
        oldData.db_product_discription2 = description_section_2
        oldData.db_product_previous_price = previous_price
        oldData.db_product_real_price = real_price
        oldData.db_product_offer_percentage = offer_percentage

        # Only update image if a new one was uploaded
        if image1:
            oldData.db_product_image1 = image1

        oldData.save()

        # ✅ Redirect back to the edit page (or any other page you like)
        return redirect('adminCardEditRead', prodid=prodIdEdit)


