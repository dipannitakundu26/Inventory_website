from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Product
# Create your views here.
def index(request):
   product_objects=Product.objects.all()
   item_name=request.GET.get('item_name')
   if item_name!='' and item_name is not None:
      product_objects=product_objects.filter(name__icontains=item_name)
   return render(request,'index.html',{'product_objects':product_objects})

class ItemdetailView(DetailView):
    model = Product
    template_name='item_detail.html'
   

    

