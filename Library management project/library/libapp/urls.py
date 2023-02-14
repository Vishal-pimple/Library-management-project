from django.urls import path
from libapp import views

urlpatterns = [
    path('', views.index),
    path('v/<rid>',views.view),
    path('delete',views.delete),
    path('udash',views.dashboard),
    path('abook',views.addbook),
    path('delete/<rid>',views.delete),
    path('edit/<rid>',views.edit),
    path('login',views.login),
    path('signup',views.signup)
]