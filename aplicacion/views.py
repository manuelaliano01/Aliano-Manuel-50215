from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .forms import * 
from .models import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth import login,authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#Vistas Generales#

def home (request):
    return render(request,"aplicacion/index.html")

@login_required
def Acerca (request):
    return render(request,"aplicacion/acerca.html")
@login_required
def Productos (request):
    return render(request,"aplicacion/productos.html")


#Almacen__________________________________________________________________________________

class AlmacenList(LoginRequiredMixin,ListView):
    model = Almacen

class AlmacenCreate(LoginRequiredMixin,CreateView):
    model = Almacen
    fields = ['nombre', 'precio', 'unidad']
    success_url = reverse_lazy('almacen')

class AlmacenUpdate(LoginRequiredMixin,UpdateView):
    model = Almacen
    fields = ['nombre', 'precio', 'unidad']
    success_url = reverse_lazy('almacen')

class AlmacenDelete(LoginRequiredMixin,DeleteView):
    model = Almacen
    success_url = reverse_lazy('almacen')

@login_required
def buscarAlmacen(request):
    return render(request, "aplicacion/almacen_buscar.html")

@login_required
def encontrarAlmacen(request):
    patron = request.GET.get("buscar")  
    if patron:
        almacen = Almacen.objects.filter(nombre__icontains=patron)
        productos_almacen = {'almacen_list': almacen}
    else:
        productos_almacen = {'almacen_list': Almacen.objects.all()}
        
    return render(request, "aplicacion/almacen_list.html", productos_almacen)

#Bebida__________________________________________________________________________________

class BebidaList(LoginRequiredMixin,ListView):
    model = Bebida

class BebidaCreate(LoginRequiredMixin,CreateView):
    model = Bebida
    fields = ['nombre', 'precio', 'unidad']
    success_url = reverse_lazy('bebidas')

class BebidaUpdate(LoginRequiredMixin,UpdateView):
    model = Bebida
    fields = ['nombre', 'precio', 'unidad']
    success_url = reverse_lazy('bebidas')

class BebidaDelete(LoginRequiredMixin,DeleteView):
    model = Bebida
    success_url = reverse_lazy('bebidas')
@login_required
def buscarBebida(request):
    return render(request, "aplicacion/bebida_buscar.html")
@login_required
def encontrarBebida(request):
    patron = request.GET.get("buscar")  
    if patron:
        bebida = Bebida.objects.filter(nombre__icontains=patron)
        productos_bebida = {'bebida_list': bebida}
    else:
        productos_bebida = {'bebida_list': Bebida.objects.all()}
        
    return render(request, "aplicacion/bebida_list.html", productos_bebida)

#Verdura__________________________________________________________________________________

class VerduraList(LoginRequiredMixin,ListView):
    model = Verdura
    
class VerduraCreate(LoginRequiredMixin,CreateView):
    model = Verdura
    fields = ['nombre', 'precio', 'unidad']
    success_url = reverse_lazy('verduras') 

class VerduraUpdate(LoginRequiredMixin,UpdateView):
    model = Verdura
    fields = ['nombre', 'precio', 'unidad']
    success_url = reverse_lazy('verduras')

class VerduraDelete(LoginRequiredMixin,DeleteView):
    model = Verdura
    success_url = reverse_lazy('verduras')
@login_required
def buscarVerdura(request):
    return render(request, "aplicacion/verdura_buscar.html")
@login_required
def encontrarVerdura(request):
    patron = request.GET.get("buscar")  
    if patron:
        verdura = Verdura.objects.filter(nombre__icontains=patron)
        productos_verdura = {'verdura_list': verdura}
    else:
        productos_verdura = {'verdura_list': Verdura.objects.all()}
        
    return render(request, "aplicacion/verdura_list.html", productos_verdura)

#Fruta____________________________________________________________________________________

class FrutaList(LoginRequiredMixin,ListView):
    model = Fruta

class FrutaCreate(LoginRequiredMixin,CreateView):
    model = Fruta
    fields = ['nombre', 'precio', 'unidad']
    success_url = reverse_lazy('frutas') 

class FrutaUpdate(LoginRequiredMixin,UpdateView):
    model = Fruta
    fields = ['nombre', 'precio', 'unidad']
    success_url = reverse_lazy('frutas')
    
class FrutaDelete(LoginRequiredMixin,DeleteView):
    model = Fruta
    success_url = reverse_lazy('frutas')
@login_required
def buscarFruta(request):
    return render(request, "aplicacion/fruta_buscar.html")
@login_required
def encontrarFruta(request):
    patron = request.GET.get("buscar")  
    if patron:
        fruta = Fruta.objects.filter(nombre__icontains=patron)
        productos_fruta = {'fruta_list': fruta}
    else:
        productos_fruta = {'fruta_list': Fruta.objects.all()}
        
    return render(request, "aplicacion/fruta_list.html", productos_fruta)

# Login____________________________________________________________________________________

def login_request(request):         
    if request.method == "POST":
        usuario = request.POST['username']
        clave = request.POST['password']
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar


            return render(request, "aplicacion/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
    
        miForm = AuthenticationForm()

    return render(request, "aplicacion/login.html", {"form": miForm} )
# Register____________________________________________________________________________________

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)

        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('login'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = RegistroForm()

    return render(request, "aplicacion/registro.html", {"form": miForm} ) 

# Editar Profile____________________________________________________________________________________

@login_required
def editProfile(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy('home'))
    else: 
        miForm = UserEditForm(instance=usuario)

    return render(request, "aplicacion/editarPerfil.html", {"form": miForm} )    
   
class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion/cambiar_clave.html"
    success_url = reverse_lazy("home")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)

        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #____________________________________________________
            avatar = Avatar(user=usuario,
                            imagen=miForm.cleaned_data["imagen"])
            avatar.save()
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            
            return redirect(reverse_lazy('home'))
    else:
    # __ Si ingresa en el else es la primera vez 
        miForm = AvatarForm()

    return render(request, "aplicacion/agregarAvatar.html", {"form": miForm} )