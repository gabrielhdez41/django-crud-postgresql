from django.urls import path
from .views import *

urlpatterns = [
    path('', registrar, name='registrar' ),
    path('listar/', listar, name='listar' ),
    path('eliminar/<int:item_id>/', eliminar, name='eliminar'),
]