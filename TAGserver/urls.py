"""TAGserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from portalAPP import views
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
#router.register(r'Usuario', views.UsuarioViewSet)
router.register(r'Projeto', views.ProjetoViewSet)
router.register(r'Noticia', views.NoticiaViewSet)
router.register(r'Evento', views.EventoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('login/', views.Login.as_view(), name='login'),
    path('Usuario/', views.UsuarioView.as_view(), name='usuario'),
    path('Usuario/<int:id>', views.usuarioDetalhe, name='usuario'),
    path('GerarLink/<str:email>', views.GerarLink.as_view(), name='gerar_link'),
    path('AutenticarLink/<str:id>', views.AutenticarLink.as_view(), name='autenticar_link'),
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)