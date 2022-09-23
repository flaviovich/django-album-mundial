from lib2to3.pgen2 import token
from django.urls import path
from .views import RegistroUsuarioView, RegistroFiguritasView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('registro', RegistroUsuarioView.as_view()),
    path('iniciar-sesion', TokenObtainPairView.as_view()),
    path('figuritas', RegistroFiguritasView.as_view())
]
