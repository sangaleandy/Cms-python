# from django.shortcuts import render
# from .models import Product, Background


# def home(request):
# 	products = Product.objects.all()
	
# 	return render(request, 'index.html', {'products':products})


# def about(request):
# 	return render(request, 'about.html', {})	

from django.shortcuts import render
from .models import Product, Background

def home(request):
    products = Product.objects.all()
    backgrounds = Background.objects.all()
    
    context = {
        'products': products,
        'backgrounds': backgrounds,
    }
    
    return render(request, 'index.html', context)

def about(request):
	return render(request, 'about.html', {})
