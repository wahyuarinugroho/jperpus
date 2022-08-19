from decimal import Context
from django.contrib.auth import forms
from django.http import request
from django.shortcuts import redirect, render, HttpResponse
from jperpustakaan.models import Buku
from jperpustakaan.forms import FormBuku, SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from jperpustakaan.resource import BukuResource
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

@login_required(login_url=settings.LOGIN_URL)
def home(request):
    template = 'home.html'
    return render(request, template)

def loginview(request):
    context = {
        'page_title': 'LOGIN',
    }
    if request.POST:
        username_login = request.POST['username']
        password_login = request.POST['password']
        user = authenticate(request, username=username_login, password=password_login) 
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')
    return render(request,'login.html', context)   

def export_xlsx(request): 
    buku = BukuResource()
    dataset = buku.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=buku.xlsx'
    return response

@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            form.save()
            messages.success(request, "user berhasil di buat!")
            # new_user = authenticate(username=username, password=password)
            # if new_user is not None:
            #     login(request, new_user)
            #     return redirect('signup')
            return redirect('signup')
        else:
            messages.error(request, "terjadi kesalahan!")
            return redirect('signup')
    else:
        form = SignUpForm()
        context = {
            'form' : form,
        }
    return render(request, 'signup.html', context)

@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, request.FILES, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Diperbaharui")
            return redirect('ubah_buku', id_buku=id_buku)
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form': form,
            'buku': buku,
        }
    return render(request, template, konteks)

@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    messages.success(request, "data berhasil dihapus")
    return redirect('buku')

@login_required(login_url=settings.LOGIN_URL)
def hapus_user(request, id_user):
    user = User.objects.filter(id=id_user)
    user.delete()
    messages.success(request, "data user berhasil dihapus")
    return redirect('users')


@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    if request.POST:
        kata_kunci = request.POST['cari']
        books = Buku.objects.filter(judul__contains=kata_kunci)
        konteks = {
            'books': books,
        }
        return render(request, 'buku.html', konteks)
    else:
        books = Buku.objects.all()
        konteks = {
            'books': books,
        }
        return render(request, 'buku.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def penerbit(request):
    return render(request, 'penerbit.html')

@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBuku()
            messages.success(request, "Data Berhasil Ditambah")
            konteks = {
                'form' : form,
            }
            return render(request,'tambah-buku.html', konteks)
    else:
        form = FormBuku()
        konteks = {
            'form': form,
        }
    return render(request, 'tambah-buku.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def users(request):
    if request.POST:
        kata_kunci = request.POST['cari_user']
        users = User.objects.filter(username__contains=kata_kunci)
        template = 'users.html'
        context = {
            'users':users,
        }
        return render(request, template, context)
    else:
        users = User.objects.all()
        template = 'users.html'
        context = {
            'users':users,
        }
        return render(request, template, context)