from django.urls import path
from.import views






urlpatterns = [
    path('', views.adminlogin, name='adminlogin'),
    path('adminindex/', views.adminindex, name='adminindex'),
    path('addbranches/', views.addbranches, name='addbranches'),
    path('branchdata/', views.branchdata, name='branchdata'),
    path('viewbranches/',views.viewbranches, name='viewbranches'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('addservice/', views.addservice,name='addservice'),
    path('servicedata/', views.servicedata,name='servicedata'),
    path('viewservice/', views.viewservice,name='viewservice'),
    path('editservice/<int:id>/',views.editservice,name='editservice'),
    path('updates/<int:id>/',views.updates,name='updates'),
    path('delete/<int:id>/',views.delete,name='delete'), 
    path('viewcontact/',views.viewcontact,name='viewcontact'), 
    path('users/',views.users,name='users'),
    path('booking-list/', views.booking_list, name='booking_list'),
]



    