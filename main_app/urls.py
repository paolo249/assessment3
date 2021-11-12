from django.urls import path
from . import views

urlpatterns = [
    path('items/create/', views.ItemsCreate.as_view(), name = 'add'),
    path('', views.ItemList.as_view(), name='item_list'),
    path('items/<int:pk>/delete/', views.ItemDelete.as_view(), name='item_delete'),
    

]