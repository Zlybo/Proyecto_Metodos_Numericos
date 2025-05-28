from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('capitulo_1/', views.capitulo_1),
    path('api/metodos_capitulo_1/', views.metodos_capitulo_1, name='api_metodos_capitulo_1'),
    path('api/informe_capitulo_1/', views.informe_capitulo_1, name='api_informe_capitulo_1'),
    path('capitulo_2/', views.capitulo_2),
    path('api/metodos_capitulo_2/', views.metodos_capitulo_2, name='api_metodos_capitulo_2'),
    path('api/informe_capitulo_2/', views.informe_capitulo_2, name='api_informe_capitulo_2'),
    path('capitulo_3/', views.capitulo_3),
    path('api/metodos_capitulo_3/', views.metodos_capitulo_3, name='api_metodos_capitulo_3'),
    path('api/grafica_capitulo_3/', views.graficar_view_3, name='grafica_capitulo_3'),

    path('api/informe_capitulo_3/', views.informe_capitulo_3, name='api_informe_capitulo_3'),

    path('grafica/', views.graficar_view, name='grafica'),
]
