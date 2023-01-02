from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('accounts/login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('history/', views.history, name='history'),
    path('books/', views.all_books, name='all_books'),
    path('books/<str:genre>/', views.bookByGenre, name='genre'),
    path('books/<str:genre>/<str:bid>/', views.viewBook, name='book'),
    path('videos/', views.all_videos, name='all_videos'),
    path('videos/<str:genre>/', views.vidByGenre, name='genre'),
    path('videos/<str:genre>/<str:vid>/', views.viewVideo, name='video'),
]
