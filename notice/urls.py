from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('myadmin/', views.administrator, name='administrator'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)