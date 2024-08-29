from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_publicaciones, name='lista_publicaciones'),
    path('<int:id>/', views.detalle_publicacion, name='detalle_publicacion'),
]
