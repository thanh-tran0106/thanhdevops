"""
URL configuration for catshelter project.

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
from . import views
from .views import upload_feline, upload_success
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view, name='home'),
    path('cat/<int:feline_id>/',views.cat_detail_view, name='cat_detail'),
    path('accounts/', include('accounts.urls', namespace='accounts')), #added namespace
    path('medical_records/',views.medical_record_search_view, name='medical_record_search'),
    path('upload/', upload_feline, name='upload_feline'),
    path('upload/success/', upload_success, name='upload_success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
