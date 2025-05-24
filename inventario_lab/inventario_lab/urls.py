"""
URL configuration for inventario_lab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""




from django.contrib import admin
from django.urls import path
from usuarios.views import login_view, dashboard_view, placeholder_view
from inventario.views import agregar_producto_view
from django.contrib.auth import views as auth_views
from inventario.views import stock_ubicaciones  # Cambia inventario por el nombre correcto de la app

#from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('productos/', agregar_producto_view, name='agregar_producto'),
    path('reportes/', placeholder_view, name='reportes'),
  
     path('stock/', stock_ubicaciones, name='stock_ubicaciones'),  # aquí la vista importada
      path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    
]

