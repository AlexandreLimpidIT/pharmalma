"""
URL configuration for pharmalma project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from .views.pharmacien_view import pharmacienV,stockPH,horairePH,renderStockPh,modifStock
from .views import product_list, home
from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('products/', product_list, name="product_list"),
    path('carte/', include('carte.urls')),
    path('pharmacie/',pharmacienV,name='pharmacie'),
    path('pharmacie/horairePH/',horairePH,name='horairePh'),
    path('pharmacie/stockPH/',stockPH,name='stockPh'),
    path('pharmacie/stockPH/modifStock',modifStock,name='modifStock'),
    path('pharmacie/<str:ref_medoc>/stockPh',renderStockPh,name='leMedoc')
]
