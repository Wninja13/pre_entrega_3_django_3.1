from django import forms
from .models import Repartidor, Tienda, Producto, Pago, Usuario, Cancelacion, Orden

class RepartidorForm(forms.ModelForm):
    class Meta:
        model = Repartidor
        fields = '__all__'

class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = '__all__'

class ProductoForm(forms.ModelForm): 
    class Meta: 
        model = Producto
        fields = '__all__'

class PagoForm(forms.ModelForm): 
    class Meta: 
        model = Pago
        fields = '__all__'

class UsuarioForm(forms.ModelForm): 
    model = Usuario
    fields = '__all__'

class CancelacionForm(forms.ModelForm): 
    model = Cancelacion
    fields = '__all__'
    
class OrdenForm(forms.ModelForm): 
    model = Orden
    fields = '__all__'


