from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Item

  
# Create your views here.
class ItemsCreate(CreateView): 
    model = Item
    fields = '__all__'
    success_url = '/'

class ItemList(ListView):
    model = Item

