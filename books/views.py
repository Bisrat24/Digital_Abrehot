import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

from .models import *


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'login': True})
    return render(request, 'home.html', {'login': False})


def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'auth/register.html', {'form': form, 'title': 'Register'})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'auth/login.html', {'title': 'Login'})


def logout_user(request):
    logout(request)
    return redirect('login')


def all_books(request):
    genres = []
    gs = BGenre.objects.all()
    for genre in gs:
        bk = Book.objects.filter(genre=genre.id)[:4]
        genres.append({genre.name: bk})

    if request.user.is_authenticated:
        return render(request, 'all_books.html', {'genres': genres, 'title': 'Books', 'login': True})
    return render(request, 'all_books.html', {'genres': genres, 'title': 'Books', 'login': False})


def bookByGenre(request, genre):
    g = BGenre.objects.get(name=genre)
    books = Book.objects.filter(genre=g.id)
    if request.user.is_authenticated:
        return render(request, 'bgenre.html', {'books': books, 'bookgenre': g.name, 'title': g.name, 'login': True})
    return render(request, 'bgenre.html', {'books': books, 'bookgenre': g.name, 'title': g.name, 'login': False})


def viewBook(request, genre, bid):
    book = Book.objects.get(id=bid)
    if request.user.is_authenticated:
        hist = History.objects.filter(book=book, user=request.user)
        if hist.exists():
            hist.update(created=datetime.datetime.now())
        else:
            hist = History()
            hist.user = request.user
            hist.book = book
            hist.save()
        return render(request, 'book.html', {'book': book, 'title': book.title, 'login': True})
    return render(request, 'book.html', {'book': book, 'title': book.title, 'login': False})


@login_required
def history(request):
    history = History.objects.filter(user=request.user.id)
    return render(request, 'history.html', {'title': 'History', 'history': history, 'login': True})


def all_videos(request):
    genres = []
    gs = VGenre.objects.all()
    for genre in gs:
        vids = Video.objects.filter(genre=genre.id)[:4]
        genres.append({genre.name: vids})
    if request.user.is_authenticated:
        return render(request, 'all_videos.html', {'genres': genres, 'title': 'Videos', 'login': True})
    return render(request, 'all_videos.html', {'genres': genres, 'title': 'Videos', 'login': False})


def vidByGenre(request, genre):
    g = VGenre.objects.get(name=genre)
    videos = Video.objects.filter(genre=g.id)
    if request.user.is_authenticated:
        return render(request, 'vgenre.html', {'videos': videos, 'videogenre': g.name, 'title': g.name, 'login': True})
    return render(request, 'vgenre.html', {'videos': videos, 'videogenre': g.name, 'title': g.name, 'login': False})


def viewVideo(request, genre, vid):
    video = Video.objects.get(id=vid)
    if request.user.is_authenticated:
        hist = History.objects.filter(video=video, user=request.user)
        if hist.exists():
            hist.update(created=datetime.datetime.now())
        else:
            hist = History()
            hist.video = video
            hist.user = request.user
            hist.save()
        return render(request, 'video.html', {'video': video, 'title': video.title, 'login': True})
    return render(request, 'video.html', {'video': video, 'title': video.title, 'login': False})
