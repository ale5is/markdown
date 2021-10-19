from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    # VIEWSET => funciona como una vista normal pero...
    # no renderiza templates, devuelve json
    queryset = Product.objects.all()
    # Model necesario para serializar (viewsets.ModelViewSet)
    serializer_class = ProductSerializer
    # serializa a json la respuesta.
    # json = JavaSCript Objects Notation
