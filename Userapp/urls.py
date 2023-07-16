from django.urls import path
from.import views





urlpatterns = [
    path('home/', views.home, name='home'),
    path('serve/<str:branchname>/',views.serve, name='serve'),
    path('detail/<str:service_name>/',views.detail,name='detail'),
    path('usercontact/',views.usercontact, name='usercontact'),
    path('getData/',views.getData,name='getData'),
    path('userregister/',views.userregister,name='userregister'),
    path('registerdata/',views.registerdata,name='registerdata'),
    path('login/',views.login,name='login'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('logout/',views.logout,name='logout'),
    path('about/',views.about,name='about'),
    path('cartdata/<int:id>/', views.cartdata, name='cartdata'),
    path('cart/',views.cart,name='cart'),
    path('cart/delete/<int:cartid>/', views.cartdelete, name='cartdelete'),
    path('booking/', views.booking, name='booking'),
    path('bookingdata/',views.bookingdata,name='bookingdata'),
    path('confirm/',views.confirm,name='confirm'),
]