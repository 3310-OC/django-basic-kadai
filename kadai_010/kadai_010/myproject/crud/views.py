from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import TemplateView, DetailView
from .models import Product


class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = Product
    template_name = "list.html"
    paginate_by = 3
    
class ProductCreateView(CreateView):
     model = Product
     fields = '__all__'
     
class ProductUpdateView(UpdateView):
     model = Product
     fields = '__all__'
     template_name_suffix = '_update_form'
     
class ProductDetailView(DetailView):
    model = Product 
    template_name = "crud/product_detail.html"
     
