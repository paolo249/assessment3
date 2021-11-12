from django.urls import path
from . import views

urlpatterns = [
    path('items/create/', views.ItemsCreate.as_view(), name = 'item_create'),
]