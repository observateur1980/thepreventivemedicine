from django.contrib import admin
from . models import Article

# Register your models here.

class ArticleModelAdmin(admin.ModelAdmin):
    fields = [
        'id',
        'publish',
        'title',
        'text',
        'articlecover',
       
        


    ]

    readonly_fields = ['id',]

    list_display = ('title',
                    'publish',)

    class Meta:
        model = Article




admin.site.register(Article, ArticleModelAdmin)