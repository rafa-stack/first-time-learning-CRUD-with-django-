from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Berita
from .forms import BeritaForm
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.messages import get_messages

def beranda(request):
    berita_terbaru = Berita.objects.order_by('-tanggal')
    return render(request, 'crudapp/beranda.html', {'berita': berita_terbaru})

def detail(request, id):
    berita = get_object_or_404(Berita, pk=id)
    return render(request, 'crudapp/detail.html', {'berita': berita})

@login_required
def tambah_berita(request):
    if request.method == 'POST':
        form = BeritaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('beranda')
    else:
        form = BeritaForm()
    return render(request, 'crudapp/tambah.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('beranda')
    else:
        form = UserCreationForm()
    return render(request, 'crudapp/register.html', {'form': form})

@login_required
def hapus_berita(request, id):
    berita = get_object_or_404(Berita, pk=id)
    berita.delete()
    return redirect('beranda')

from django.contrib import messages

from django.contrib import messages
from django.contrib.messages import get_messages

@login_required
def hapus_akun(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if request.user.check_password(password):
            request.user.delete()
            return redirect('beranda')
        else:
            messages.error(request, 'Password salah! Akun tidak dihapus.')
            return redirect('hapus_akun')

    # Bersihkan pesan lama saat GET
    storage = get_messages(request)
    list(storage)  # ini akan mengkonsumsi semua pesan agar tidak muncul otomatis

    return render(request, 'crudapp/hapus_akun.html')
# Create your views here.
