from django.urls import path
from .views import list_books, library_detail, register_view, login_view, logout_view

urlpatterns = [
    path('', list_books, name='list_books'),
    path('library/<int:library_id>/', library_detail, name='library_detail'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]