from rest_framework import serializers

from goods.models import Goods,GoodsCategory





class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    # images = GoodsImageSerializer(many=True)
    class Meta:
        model = Goods
        fields = "__all__"
