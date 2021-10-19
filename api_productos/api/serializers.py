from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        # fields = [name', 'price', 'description'] para especificar campo
        # exclude = ['created', 'updated'] para excluir campo