from django.shortcuts import render
from .models import Service

# Create your views here.


def services(request):
    services = Service.objects.all()  # Esquivale a hacer un select
    # La clave puede ser diferente, la variable tiene que ser exacta a la establecida
    return render(request, "services/services.html", {'services': services})
