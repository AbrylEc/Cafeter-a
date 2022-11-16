from .models import Social


def ctx_dict(request):
    ctx = {'test': "Hola mundo"}
    socialList = Social.objects.all()
    # Agregar datos en el diccionario
    for social in socialList:
        ctx[social.key] = social.url
    return ctx
