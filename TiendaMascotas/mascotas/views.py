from django.shortcuts import render, redirect
from .models import Cliente, Producto
from .forms import ClienteForm, ProductoForm
# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)
def home(request):

    return render(request, 'index.html')

def catalogo(request):

    return render(request, 'catalogo.html')

def quienes_somos(request):

    return render(request, 'quienes_somos.html')

def registro(request):

    return render(request, 'registro.html')

def api(request):

    return render(request, 'api.html')

def mostrar(request):
    cliente = Cliente.objects.all()

    datos = {
        'cliente': cliente
    }
    return render(request, 'mostrar.html', datos)

def form_cliente(request):
    if request.method=='POST': 
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect('home')
    else:
        cliente_form= ClienteForm()
    return render(request, 'form_crear_cliente.html', {'cliente_form': cliente_form})

def form_mod_cliente(request, id): 
    cliente = Cliente.objects.get(rut=id)
    datos = {
        'form': ClienteForm(instance=cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data = request.POST, instance=cliente)
        if formulario.is_valid: 
            formulario.save()
            return redirect ('mostrar')
    return render (request, 'form_mod_cliente.html', datos )


def form_del_cliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect ('mostrar')


def mostrar2(request):
    producto = Producto.objects.all()

    datos = {
        'producto': producto
    }
    return render(request, 'mostrar2.html', datos)

def form_producto(request):
    if request.method=='POST': 
        producto_form = ProductoForm(request.POST)
        if producto_form.is_valid():
            producto_form.save()
            return redirect('home')
    else:
        producto_form= ProductoForm()
    return render(request, 'form_crear_producto.html', {'producto_form': producto_form})

def form_mod_producto(request, id): 
    producto = Producto.objects.get(idProducto=id)
    datos = {
        'form': ProductoForm(instance=producto)
    }
    if request.method=='POST':
        formulario = ProductoForm(data = request.POST, instance=producto)
        if formulario.is_valid: 
            formulario.save()
            return redirect ('mostrar2')
    return render (request, 'form_mod_producto.html', datos )


def form_del_producto(request, id):
    producto = Producto.objects.get(idProducto=id)
    producto.delete()
    return redirect ('mostrar2')