

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm
#from inventario.views import stock_ubicaciones
from django.http import HttpResponse

@login_required
def agregar_producto_view(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductoForm()
    return render(request, 'inventario/agregar_producto.html', {'form': form})




def stock_ubicaciones(request):
    context = {
        'mensaje': 'Aquí verás el stock y las ubicaciones',
    }
    return render(request, 'inventario/stock_ubicaciones.html', context)