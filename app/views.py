from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, "app/inicio.html")

def registrate(request):
    return render(request, "app/registrate.html",)

def comprar(request):
    return render(request, "app/comprar.html")

def vender(request):
    return render(request, "app/vender.html")

def catalogo(request):
    contexto = {'piezas': Pieza.objects.all() }
    return render(request, "app/catalogo.html", contexto)

def PiezaForm(request):
    if request.method == "POST":
        formulario = PiezasForm(request.POST)
        if formulario.is_valid():
            piezaNombre = formulario.cleaned_data.get("nombre")
            piezaDescripcion = formulario.cleaned_data.get("descripcion")
            piezaPrecio = formulario.cleaned_data.get("precio")
            piezaDimensiones = formulario.cleaned_data.get("dimensiones")
            piezaTecnica = formulario.cleaned_data.get("tecnica")
            
        
            pieza = Pieza(nombre=piezaNombre,
                            descripcion=piezaDescripcion,
                            precio=piezaPrecio,
                            dimensiones=piezaDimensiones,
                            tecnica=piezaTecnica,
                            
                            )
            pieza.save()
                           
            return render(request, "app/piezaform.html")

    else:
        formulario = PiezasForm()

    return render(request, "app/piezaform.html", {"form":formulario})

def ComprarForm(request):
    if request.method == "POST":
        formulario = CompradorForm(request.POST)
        if formulario.is_valid():
            compradorUsuario = formulario.cleaned_data.get("usuario")
            compradorNombre = formulario.cleaned_data.get("nombre")
            compradorDireccion = formulario.cleaned_data.get("direccion")
            compradorCorreo = formulario.cleaned_data.get("correo")
            compradorTelefono = formulario.cleaned_data.get("telefono")
            
        
            comprador = Comprador(usuario=compradorUsuario,
                            nombre=compradorNombre,
                            direccion=compradorDireccion,
                            correo=compradorCorreo,
                            telefono=compradorTelefono,
                            
                            )
            comprador.save()
                           
            return render(request, "app/inicio.html")

    else:
        formulario = CompradorForm()

    return render(request, "app/compradorform.html", {"form":formulario})

def VenderForm(request):
    if request.method == "POST":
        formulario = VendedorForm(request.POST)
        if formulario.is_valid():
            vendedorUsuario = formulario.cleaned_data.get("usuario")
            vendedorNombre = formulario.cleaned_data.get("nombre")
            vendedorCorreo = formulario.cleaned_data.get("correo")
            vendedorTelefono = formulario.cleaned_data.get("telefono")
            
        
            vendedor = Vendedor(usuario=vendedorUsuario,
                            nombre=vendedorNombre,
                            correo=vendedorCorreo,
                            telefono=vendedorTelefono,
                            
                            )
            vendedor.save()
                           
            return render(request, "app/inicio.html")

    else:
        formulario = VendedorForm()

    return render(request, "app/vendedorform.html", {"form":formulario})




def buscarPieza(request):
    return render(request, "app/buscarPieza.html")

def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        tecnica = Pieza.objects.filter(tecnica__icontains=patron)
        contexto = {"piezas": tecnica}
        return render(request, "app/catalogo.html", contexto)
    return HttpResponse("No se ingreso nada a buscar")
