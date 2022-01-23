from django.contrib import admin
from .models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user_id', 'status', 'updated_date')
    list_filter = ('status',)
    search_fields = ('title', 'text')
    ordering = ('-updated_date',)

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Social_medial)
admin.site.register(SliderImage)
admin.site.register(AboutMe)