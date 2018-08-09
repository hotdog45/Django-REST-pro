from rest_framework import serializers

from goods.models import Goods,GoodsCategory,Banner,GoodsImage





class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ("image", )

class GoodsSerializers(serializers.ModelSerializer):
    category = CategorySerializers()
    images = GoodsImageSerializer(many=True)
    class Meta:
        model = Goods
        fields = "__all__"

class BannerSerializers(serializers.ModelSerializer):

    class Meta:
        model = Banner
        fields = "__all__"