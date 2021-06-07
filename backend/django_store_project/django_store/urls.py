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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

# jwt
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from rest_framework.routers import DefaultRouter

# documentation
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

import store.views
import users.views
import orders.views
import posts.views

router = DefaultRouter()
router.register(r'posts', posts.views.PostViewSet, basename='posts')

urlpatterns = [
    # authorization, authentication
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/logout/blacklist/',
         users.views.BlacklistTokenView.as_view(), name='blacklist'),
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v1/users/register/',
         users.views.UserCreate.as_view(), name='create_user'),

    # content
    path('api/v1/games/', store.views.GameAPIView.as_view(), name='games'),
    path('api/v1/games/<int:id>/',
         store.views.GameDetailAPIView.as_view(), name='game'),
    path('api/v1/genres/', store.views.GenreAPIView.as_view(), name='genres'),

    # orders
    path('api/v1/orders/', orders.views.OrderView.as_view(), name='orders'),
    path('api/v1/checkout/', orders.views.Checkout.as_view(), name='checkout'),
    # path('api/v1/orders/<int:pk>', orders.views.DetailOrder.as_view(), name='order'),

    # posts
    path('api/v1/', include(router.urls)),

    # documentation
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
