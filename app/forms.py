from django import forms

class PiezasForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    descripcion = forms.CharField(max_length=200, required=True)
    precio = forms.IntegerField(required=True)
    dimensiones = forms.CharField(max_length=10, required=True)
    tecnica = forms.CharField(max_length=30, required=True)


class CompradorForm(forms.Form):
     usuario = forms.CharField(max_length=50, required=True)
     nombre = forms.CharField(max_length=50, required=True)
     direccion = forms.CharField(max_length=50, required=True)
     correo =forms.EmailField(max_length=50, required=True)
     telefono = forms.IntegerField(required=True)



class VendedorForm(forms.Form):
     usuario = forms.CharField(max_length=50, required=True)
     nombre = forms.CharField(max_length=50, required=True)
     correo =forms.EmailField(max_length=50, required=True)
     telefono = forms.IntegerField(required=True)