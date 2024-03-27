
from django.urls import path, include
from .views import*



from django.contrib.auth.views import LogoutView

urlpatterns = [
    
#Vistas Generales#
path('', home, name="home"),
path('acerca', Acerca, name="acerca"),
path('promo', Productos, name="promo"),

#Almacen_________________________________________________________________________
path('almacen/', AlmacenList.as_view(), name="almacen" ),
path('almacen_create/', AlmacenCreate.as_view(), name="almacen_create" ),
path('almacen_update/<int:pk>/', AlmacenUpdate.as_view(), name="almacen_update" ),
path('almacen_delete/<int:pk>/', AlmacenDelete.as_view(), name="almacen_delete" ),
path('buscar_almacen/', buscarAlmacen,name="buscar_almacen"),
path('encontrar_almacen/', encontrarAlmacen,name="encontrar_almacen"),

#Bebida_________________________________________________________________________
 path('bebidas/', BebidaList.as_view(), name="bebidas" ),
 path('bebidas_create/', BebidaCreate.as_view(), name="bebidas_create" ),
 path('bebidas_update/<int:pk>/', BebidaUpdate.as_view(), name="bebidas_update" ),
 path('bebidas_delete/<int:pk>/', BebidaDelete.as_view(), name="bebidas_delete" ),
path('buscar_bebida/', buscarBebida,name="buscar_bebida"),
path('encontrar_bebida/', encontrarBebida,name="encontrar_bebida"),

#Verdura_________________________________________________________________________
path('verduras', VerduraList.as_view(), name="verduras"),
path('verduras_create/', VerduraCreate.as_view(), name="verduras_create" ),
path('verduras_update/<int:pk>/', VerduraUpdate.as_view(), name="verduras_update" ),
path('verduras_delete/<int:pk>/', VerduraDelete.as_view(), name="verduras_delete" ),
path('buscar_verdura/', buscarVerdura,name="buscar_verdura"),
path('encontrar_verdura/', encontrarVerdura,name="encontrar_verdura"),

#Fruta_________________________________________________________________________
path('frutas', FrutaList.as_view(), name="frutas"),
path('frutas_create/', FrutaCreate.as_view(), name="frutas_create" ),
path('frutas_update/<int:pk>/', FrutaUpdate.as_view(), name="frutas_update" ),
path('frutas_delete/<int:pk>/', FrutaDelete.as_view(), name="frutas_delete" ),
path('buscar_fruta/', buscarFruta,name="buscar_fruta"),
path('encontrar_fruta/', encontrarFruta,name="encontrar_fruta"),

#Login,Register__________________________________________________________________
path('login/', login_request, name="login"),
path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html") , name="logout"),
path('registrar/', register, name="registrar"),
#Editar Perfil__________________________________________________________________
path('perfil/', editProfile, name="perfil"),
path('<int:pk>/password/', CambiarClave.as_view(), name="cambiar_clave"),
path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
]

