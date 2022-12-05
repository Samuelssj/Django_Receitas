from django.urls import path
from . import views
from .models import Receita

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita')
]
