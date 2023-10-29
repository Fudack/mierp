from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Productos

# Create your views here.

@login_required(login_url='inicio')
def inventario(request):
    form = ProductForm()
    productos = Productos.objects.all()
    
    if request.method == 'POST':
        print(request.POST)
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    
    context = {
        'productos': productos,
        'form': form
    }
    return render(request, 'inventario.html', context)