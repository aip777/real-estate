from django.contrib import admin

# Register your models here.
from .models import Book


class BookAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'title', 'author', 'address', 'phone', 'pdf', 'cover')
  list_display_links = ('id', 'name')
  list_filter = ('name',)

  search_fields = ('title', 'name', 'author')
  list_per_page = 25



admin.site.register(Book, BookAdmin)
