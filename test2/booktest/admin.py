from django.contrib import admin

from booktest.models import BookInfo,HeroInfo

class HeroInfoInLine(admin.TabularInline):
    model = HeroInfo
    extra = 2


class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id','btitle','bpub_date']
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10
    fields = ['bpub_date', 'btitle']
    inlines = [HeroInfoInLine]

admin.site.register(BookInfo,BookInfoAdmin)

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','hname','hgenger','hcontent','hbook']
    list_filter = ['hname']
    search_fields = ['hname']
admin.site.register(HeroInfo,HeroInfoAdmin)