from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('items/create/', views.ItemsCreate.as_view(), name = 'item_create'),
    path('', views.ItemList.as_view(), name='item_list'),

]