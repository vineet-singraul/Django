from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # Befor Login Ke liye hai 
    path('',views.home,name='home'),
    path('mens/',views.mens,name='mens'),
    path('womens/',views.womens,name='womens'),
    path('kides/',views.kides,name='kides'),
    path('electranics/',views.electranics,name='electranics'),
    path('grousary/',views.grousary,name='grousary'),

    #  ............. ADMIN OR USER KE LOGIN OR SIGNUP KE LIYE ........................ 
    path('login/',views.login,name='login'),     # Admin or uaer ke login ke liye
    path('signup/',views.signup,name='signup'),  # keval user account banane ke liye

    # After Login Ke liye hai 
    path('home/<int:pk>',views.home1,name='home1'),
    path('mens/<int:pk>',views.mens1,name='mens1'),
    path('womens/<int:pk>',views.womens1,name='womens1'),
    path('kides/<int:pk>',views.kides1,name='kides1'),
    path('electranics/<int:pk>',views.electranics1,name='electranics1'),
    path('grousary/<int:pk>',views.grousary1,name='grousary1'),

    # ............User Desh Bord Ka Code Path all hare .....................
    path('deshbord/<int:pk>/', views.deshbord, name='deshbord'),        # user Deshbord ke liye 
    path('query/<int:pk>',views.query,name='query'),                    # Query ke liye path
    path('allquery/<int:pk>',views.allquery,name='allquery'),           # all Query ko print ksrne ke liye
    path('edit/<int:pk>/',views.edit,name='edit'),                      # Edit Ke Liye
    path('quaryupdate/<int:pk>/',views.quaryupdate,name='quaryupdate'), # vahi edit jo aaya hai update karene ke liye
    path('delete/<int:pk>/',views.delete,name='delete'),                # Delete Ke Liye
    path('/<int:pk>/',views.search,name='search'),                      # Search ke liye:
    path('offer/<int:pk>/', views.offer, name='offer'),                 # deshbord me path offer ke liye


    #  ........ CARD OR NEW PAGE BANAKE KE LIYE (addcard,showCart,showIDdetails)...........
    path('addcard/<int:pk>/<int:jk>/', views.addcard, name='addcard'),        # add to card karne ke liye
    path('showCart/<int:pk>/',views.showCart,name='showCart'),                # Show Card Ke Liye Hai Ye
    path('cardDelete/<int:pk>/<int:jk>/',views.cardDelete,name='cardDelete'), # Cards ko delete karne ke liye :
    path('showIDdetails/<int:pk>/<int:jk>/', views.showIDdetails, name='showIDdetails'),  # Single Card ki detail dikhane ke liye
    path('goForPayment/<int:pk>/<int:cd>/',views.goForPayment,name='goForPayment'),  # Card ki -->  pk and user ki --> cd

    # Admin Deshbord ke liye hai ye code
    path('adminDeshbord/',views.adminDeshbord,name='adminDeshbord'),
    path('homead',views.homead,name='homead'),           # Admin ke home ke liye
    path('mensad',views.mensad,name='mensad'),           # Admin ke mens ke liye     
    path('womensad',views.womensad,name='womensad'),     # Admin ke women ke liye
    path('kidesad',views.kidesad,name='kidesad'),        # Admin ke kides ke liye
    path('electanicad',views.electanicad,name='electanicad'),# Admin ke electranic ke liye
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)