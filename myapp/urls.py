from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inicio'),
    path('home/', views.home, name='home'),
    path('herramienta/', views.index, name='herramienta'),
    path('createAnalisis/', views.createAnalisis, name='createAnalisis'),
    path('deleteAnalisis/<int:id>/', views.deleteAnalisis, name='deleteAnalisis'),
    path('exportarAnalisis', views.export_to_excel, name='exportarAnalisis'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('user/', views.viewUser, name='verPerfil'),
    path('soporte/', views.soporte, name='soporte'),
    path('recuperar_clave/', views.recuperar_clave, name='recuperar_clave'),
    path('restablecer_clave/', views.restablecer_clave, name='restablecer_clave'),
    
    path('getUser/<int:id>', views.getUser),
    # se puede usar int o str como tipo de dato
    path('hola/<str:nombre>', views.ejemploconcatena)
]