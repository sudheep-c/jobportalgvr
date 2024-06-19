from django.urls import path
from.import views

urlpatterns = [

    path('',views.index1,name="index1"),
    path('register/',views.register,name="register"),
    path('login/',views.loginn,name="login"),
    

]
