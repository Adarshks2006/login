from loginapp import views
from django.urls import path,include

urlpatterns = [

    path('',views.newlogin,name='newlogin'),
    path('adduser',views.adduser,name='adduser'),
    path('newsign',views.newsign,name='newsign'),
    path('addsign',views.addsign,name='addsign'),
    path('afterlogin',views.afterlogin,name='afterlogin'),
    path('userlogout',views.userlogout,name='userlogout'),

  
]
