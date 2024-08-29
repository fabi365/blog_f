from django.shortcuts import render
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post

def lista_publicaciones(request):
    publicaciones = Post.objects.all()

    # Filtrar por categoría y fecha
    categoria = request.GET.get('categoria')
    if categoria:
        publicaciones = publicaciones.filter(categoria__icontains=categoria)

    fecha = request.GET.get('fecha_publicacion')
    if fecha:
        publicaciones = publicaciones.filter(fecha_publicacion=fecha)

    # Buscar por título o contenido
    query = request.GET.get('q')
    if query:
        publicaciones = publicaciones.filter(titulo__icontains=query) | publicaciones.filter(contenido__icontains=query)

    # Paginación
    paginator = Paginator(publicaciones, 10)  # Mostrar 10 publicaciones por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'posts/lista_publicaciones.html', {'page_obj': page_obj})


# Create your views here.
