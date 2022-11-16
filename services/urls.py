from django.urls import path
from . import views

urlpatterns = [
    # Se retira el services de aquí para evitar la redundancia
    # path('services/', views.services, name="services"),
    path('', views.services, name="services"),
]
