from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Movie,Review

admin.site.register(Movie)
# class MovieAdmin(admin.ModelAdmin):
#     list_display = ('id','title','description')
#     search_fields = ['title', 'description']
#     list_editable = ('description',)
# admin.site.register(Movie,MovieAdmin)
admin.site.register(Review)