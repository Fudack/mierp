from django import forms
from .models import Productos


#funcion para crear un nuevo producto
class ProductForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'
