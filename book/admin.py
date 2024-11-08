# from django.contrib import admin
# from .models import Book
# # admin.site.register(Book)
#
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('id','title','description')
#     search_fields = ['title', 'description']
#     list_editable = ('description',)
# admin.site.register(Book,BookAdmin)

from django.contrib import admin
from .models import Book, ReviewBook

admin.site.register(Book)
admin.site.register(ReviewBook)