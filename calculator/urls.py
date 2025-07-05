from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.loginpage,name='login'),
    path('register/',views.registerpage,name='register'),
    path('calci/',views.calci,name='calci'),
    path('result/<int:a>/<int:b>/<str:resu>/',views.result,name='result')
]