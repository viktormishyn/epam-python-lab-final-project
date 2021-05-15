"""django_store URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include
from django.contrib import admin
from django.urls import path
from rest_framework import views
import store.views
import users.views
from django.conf import settings
from django.conf.urls.static import static
# jwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/games/', store.views.GameAPIView.as_view(), name='games'),
    path('api/v1/games/<int:id>/',
         store.views.GameDetailAPIView.as_view(), name='game'),
    path('api/v1/genres/', store.views.GenreAPIView.as_view(), name='genres'),
    path('api/v1/users/register/',
         users.views.UserCreate.as_view(), name='create_user'),
    path('api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/logout/blacklist/',
         users.views.BlacklistTokenView.as_view(), name='blacklist'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
