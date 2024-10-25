from django.urls import path
from .views import vista_about
from .views import vista_bio
from .views import vista_inicio
from .views import vista_lista_producto
from .views import vista_agregar_producto
from .views import vista_ver_producto
from .views import vista_editar_producto
from .views import vista_eliminar_producto
from .views import vista_login
from .views import vista_logout
from .views import vista_register
from .views import vista_perfil
from .views import vista_raiz
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', vista_raiz, name='vista_raiz'),
    path('login/', vista_login, name='vista_login'),
    path('inicio/', (vista_inicio), name='vista_inicio'),
    path('about/', (vista_about), name='vista_about'),
    path('bio/', (vista_bio), name='vista_bio'),
    path('lista_producto/', (vista_lista_producto), name='vista_lista_producto'),
    path('agregar_producto/', (vista_agregar_producto), name='vista_agregar_producto'),
    path('ver_producto/<int:id_prod>/', (vista_ver_producto), name='vista_ver_producto'),
    path('editar_producto/<int:id_prod>/', (vista_editar_producto), name='vista_editar_producto'),
    path('eliminar_producto/<int:id_prod>/', (vista_eliminar_producto), name='vista_eliminar_producto'),   
    path('logout/', vista_logout, name='vista_logout'),
    path('register/', vista_register, name='vista_register'),
    path('perfil/', (vista_perfil), name='vista_perfil'),




]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)