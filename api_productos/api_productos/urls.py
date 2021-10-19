from django import urls
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework import routers

# Creamos el router que va a controlar los endpoints
router = routers.DefaultRouter()
# Registramos el router
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),

    path('api/v1/', include('rest_auth.urls')),
    path('api/v1/registration', include('rest_auth.registration.urls')),   
]
