"""djorg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth.models import User
from django.urls import include, path, re_path
from rest_framework import routers, serializers, viewsets
from notes.serializer import PersonalNoteViewSet
from notes.views import index
from . import views

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'is_superuser')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'notes', PersonalNoteViewSet)

app_name='home'
urlpatterns = [
    path('notes/', include('notes.urls')),
    path('admin/', admin.site.urls),
    re_path(r'^api/', include(router.urls)),
    re_path(r'^accounts/', include('allauth.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls')),
    path('', views.Home.as_view(), name='home'),

    # re_path(r'^graphql/', GraphQLView.as_view(graphiql=True)),
]
