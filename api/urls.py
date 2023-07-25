from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('notes/', views.getNotes),
    path('notes/create/', views.createNote), # Make sure this comes before getNote because the url is expecting a primary key and it will give error that create was passed if we visit this url
    path('notes/<str:pk>/', views.getNote),
    path('notes/<str:pk>/update/', views.updateNote),
    path('notes/<str:pk>/delete/', views.deleteNote),
]