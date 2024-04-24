from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('users/', views.users),
    path('getUser/<int:id>', views.getUser),
    path('createIntroduction/', views.createIntroduction, name='createIntroduction'),
    path('signup/', views.signup, name='signup'),


    # se puede usar int o str como tipo de dato
    path('hola/<str:nombre>', views.ejemploconcatena)
]