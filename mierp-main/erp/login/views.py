from django.urls import reverse_lazy
from .forms import CustomUserCreationForm,  CustomAuthenticationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required


class CustomLogoutView(LoginView):
    template_name = 'logout.html'
    success_url = reverse_lazy('inicio')
    next_page = 'home'  # Redirige a la página de índice después de cerrar sesión


def home(request):
    return render(request, 'home.html')

def inicio(request):
    form = CustomAuthenticationForm()
    
    context = {'form': form}
    
    if request.POST:
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
            return redirect('home')
        else:
            context['error'] = 'Provide valid credentials'
            return render(request, 'registro/login.html', context)
    else:
        print('No POST')
                
    return render(request, 'registro/login.html', context)

@login_required
def productos(request):
    return render(request, 'productos.html')

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registro/registro.html', data)

