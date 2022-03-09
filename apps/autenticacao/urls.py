from django.urls import path
from . import views 

urlpatterns = [
    path('logout/', views.logout_request, name='sair'),
    path('logar/', views.login, name='logar'),

    path('', views.signIn),
    path('postsignIn/', views.postsignIn),
    path('signUp/', views.signIn, name="signup"),
    path('logout/', views.logout, name="log"),
    path('postsignUp/', views.postsignUp, name='cadastre_se'),
    
    path('reset/', views.reset, name='resetar_senha'),
    path('postReset/', views.postReset, name='reset_password'),
]
