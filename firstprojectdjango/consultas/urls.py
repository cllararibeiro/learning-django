from django.urls import path
from .views import lista_consultas, criar_consulta, deletar_consulta, editar_consulta

urlpatterns = [
    path('', lista_consultas, name='lista_consultas'),
    path('nova/', criar_consulta, name='criar_consulta'),
    path('deletar/<int:id>/', deletar_consulta, name='deletar_consulta'),
    path('editar/<int:id>/', editar_consulta, name='editar_consulta'),
]