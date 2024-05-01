from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('home/', views.home, name='home'),
    path('createAnalisis/', views.createAnalisis, name='createAnalisis'),
    path('deleteAnalisis/<int:id>/', views.deleteAnalisis, name='deleteAnalisis'),
    path('exportarAnalisis', views.export_to_excel, name='exportarAnalisis'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('user/', views.viewUser, name='verPerfil'),
    path('soporte/', views.soporte, name='soporte'),
    
    path('getUser/<int:id>', views.getUser),
    # se puede usar int o str como tipo de dato
    path('hola/<str:nombre>', views.ejemploconcatena)
]