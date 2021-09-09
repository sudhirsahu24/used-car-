from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('result/', views.result, name='result'),
    path('intro/', views.intro, name='intro'),
    path('methods/', views.methods, name='methods'),
    path('eda/', views.eda, name='eda'),
    path('cor/', views.cor, name='cor'),
    path('nullvalue/', views.nullvalue, name='nullvalue'),
    path('data/', views.data, name='data'),
    path('outlier/', views.outlier, name='outlier'),
    path('accuracy/', views.accuracy, name='accuracy'),
    path('contact/', views.contact, name='contact'),


]