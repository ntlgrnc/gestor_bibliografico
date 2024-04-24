from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users/', views.users),
    path('getUser/<int:id>', views.getUser),
    path('createIntroduction/', views.createIntroduction, name='createIntroduction'),


    # se puede usar int o str como tipo de dato
    path('hola/<str:nombre>', views.ejemploconcatena)
]