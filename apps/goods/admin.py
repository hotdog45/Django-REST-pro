from django.contrib import admin

# Register your models here.
from goods.models import GoodsCategory
from goods.models import GoodsCategoryBrand
from goods.models import Goods
from goods.models import GoodsImage
from goods.models import Banner
from goods.models import HotSearchWords



admin.site.register(GoodsCategory)
admin.site.register(GoodsCategoryBrand)
admin.site.register(Goods)
admin.site.register(GoodsImage)
admin.site.register(Banner)
admin.site.register(HotSearchWords)