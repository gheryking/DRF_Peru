from rest_framework import serializers

from apps.products.models import Product
from apps.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer


class ProductSerializer(serializers.ModelSerializer):
    # measure_unit = serializers.StringRelatedField()
    # category_product = serializers.StringRelatedField()
    class Meta:
        model = Product
        exclude = ('state', 'create_date', 'modified_date', 'delete_date')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'description': instance.description,
            'image': instance.image if instance.image != '' else '',
            'measure_unit': instance.measure_unit.description,
            'category_product': instance.category_product.description
        }
