from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import request
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
#from reportlab.lib.pagesizes.letters


from .models import TrabajadorModel
from .forms import UserRegisterForm, TrUpdateForm, RegistroTrabajadorForm, UserLoginForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def registerUser_view(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        email = request.POST.get('email', '')
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
            messages.success(request, 'Usuario registrado con éxito')
            return redirect('index')
        else:
            messages.error(request, 'Usuario no registrado')

    else:
        form = UserRegisterForm()       
    return render(request, 'auth/register.html', {'form': form})

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, 'Usuario logueado exitosamente')
        return redirect('listar')            
    return render(request, 'auth/login.html', {'user': user})




def register_view(request):
    return render(request, 'main/register.html', {'title': 'Registro'})

@login_required
def listar_view(request):
    if request.method == 'GET':
        ctx = TrabajadorModel.objects.all()
        paginator = Paginator(ctx, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'main/listar.html', {'page_obj': page_obj})

    return render(request, 'main/listar.html', {'title': 'Listado'}, {'page_obj': page_obj})


def edit_view(request, id):
    id = TrabajadorModel.objects.get(id=id)
    form = TrUpdateForm(instance=id)
    
    if request.method == 'POST':
        form = TrUpdateForm(request.POST or None, instance=id)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, "Registro Actualizado")
            
    else:
        form = TrUpdateForm(request.POST, instance=id)
    return render(request, 'main/update.html', {'id': id, 'form': form})
    

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    else:
        return HttpResponse('usuario no autenticado')




def create_pdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(100, 100, "Hola mundo")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hola.pdf")

