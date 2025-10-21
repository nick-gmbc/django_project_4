"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from dice import views as dice_views
from table import views as table_views

urlpatterns = [
    path('', dice_views.throw_dice, name='throw_dice'),
    path('show_table/', table_views.show_table, name='show_table'),
    path('throw_dice/', dice_views.throw_dice, name='throw_dice'),
    path('admin/', admin.site.urls),
]
