from django.urls import path
from android_rest import views

urlpatterns = [
    path('list',views.list,name="list"),
    path('loginandroid',views.loginandroid,name="loginandroid"),
]