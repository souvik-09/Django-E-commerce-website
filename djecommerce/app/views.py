from itertools import product
from unicodedata import category
from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages

class ProductView(View):
    def get (self, request):
        topwears = Product.objects.filter(category = 'TW')
        bottomwears = Product.objects.filter(category = 'BW')
        mobiles = Product.objects.filter(category = 'M')
        laptops = Product.objects.filter(category = 'L')
        return render (request, 'app/home.html', {'topwears': topwears, 'bottomwears': bottomwears, 'mobiles': mobiles, 'laptops': laptops})


#def product_detail(request):
 #return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get (self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product': product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def mobile(request, data = None):
 if data == None:
    mobiles = Product.objects.filter(category = 'M')
 elif data == 'Xiaomi' or data == 'Samsung' or data == 'Motorola' or data == 'Apple' or data == 'Oneplus':
    mobiles = Product.objects.filter(category = 'M'). filter(brand = data)
 elif data == 'below':
    mobiles = Product.objects.filter(category = 'M'). filter(discounted_price__lt =10000) 
 elif data == 'above':
    mobiles = Product.objects.filter(category = 'M'). filter(discounted_price__gt =10000)      
 return render(request, 'app/mobile.html', {'mobiles': mobiles})

def laptop(request, data = None):
 if data == None:
    laptops = Product.objects.filter(category = 'L')
 elif data == 'Apple' or data == 'Hp' or data == 'Lenovo' or data == 'Asus' or data == 'MSI':
    laptops = Product.objects.filter(category = 'L'). filter(brand = data)
 elif data == 'below':
    laptops = Product.objects.filter(category = 'L'). filter(discounted_price__lt =50000) 
 elif data == 'above':
    laptops = Product.objects.filter(category = 'L'). filter(discounted_price__gt =50000) 
 return render(request, 'app/laptop.html', {'laptops': laptops})

def topwears(request, data = None):
 if data == None:
    topwears = Product.objects.filter(category = 'TW')
 return render(request, 'app/topwears.html', {'topwears': topwears})

def bottomwears(request, data = None):
 if data == None:
    bottomwears = Product.objects.filter(category = 'BW')
 return render(request, 'app/bottomwears.html', {'bottomwears': bottomwears})


class CustomerRegistrationView(View):
   def get(self, request):
      form = CustomerRegistrationForm()
      return render(request, 'app/customerregistration.html',{'form': form})
   def post(self, request):
      form = CustomerRegistrationForm(request.POST)
      if form.is_valid():
         messages.success(request, 'Congratulations! Registered Successfully')
         form.save()
      return render(request, 'app/customerregistration.html',{'form': form})

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')

class ProfileView(View):
   def get (self, request):
      form = CustomerProfileForm()
      return render(request, 'app/profile.html', {'form': form})
