"""
URL configuration for inventario_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include 
from email_service.api.views import EmailAPIView





urlpatterns = [


    path('send-email/', EmailAPIView.as_view(), name='send-email'),
    path('admin/', admin.site.urls),
    path('api/', include('reporte_tecnico.api.urls')),
    path('api/', include('tipo_movimiento.api.urls')),
    path('api/', include('rol.api.urls')),
    path('api/', include('usuario.api.urls')),
    path('api/', include('propiedad.api.urls')),
    path('api/', include('local.api.urls')),
    path('api/', include('area_responsable.api.urls')),
    path('api/', include('area.api.urls')),
    path('api/', include('clasificacion.api.urls')),
    path('api/', include('estado.api.urls')),
    path('api/', include('caracteristica.api.urls')),
    path('api/', include('categoria.api.urls')),
    path('api/', include('marca.api.urls')),
    path('api/', include('propiedad_baja.api.urls')),

  
    
   
  
]
