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
from .views.pharmacien_view import pharmacienV, horairePH, modifier_horaire, renderStockPh, updateStock
from .views.home_views import home, pharmacie_redirect_view
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('carte/', include('carte.urls')),
    path('pharmacie/<int:pharmacie_id>/horairePH/',horairePH,name='horairePh'),
    path('pharmacie/<int:pharmacie_id>/modifier_horaire/<int:horaire_id>/', modifier_horaire, name='modifier_horaire'),
    path('pharmacie/<int:pharmacie_id>/stockPh/<str:ref_medoc>',renderStockPh,name='leMedoc'),
    path('pharmacie/<int:pharmacie_id>/stockPh/<str:ref_medoc>/update/', updateStock, name='update_stock'),
    path('pharmacie/<int:pharmacie_id>/', pharmacienV, name='pharmacie_detail'),
    path('redirect/', pharmacie_redirect_view, name='pharmacie_redirect'),
]
