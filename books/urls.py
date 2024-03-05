from django.urls import path
from . import views
from django.views.generic import TemplateView

# path: /books/
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('', views.book_list, name='book_list'),
    path('create/', views.book_create, name='book_create'),
    path('update/<int:pk>/', views.book_update, name='book_update'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
]
