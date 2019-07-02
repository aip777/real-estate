from django.contrib import admin

# Register your models here.
from .models import blog


class BlogAdmin(admin.ModelAdmin):
  list_display = ('id', 'title_one', 'description_one', 'is_published', 'photo_main', 'list_date')
  list_display_links = ('id', 'title_one')
  list_filter = ('title_one',)
  list_editable = ('is_published',)

  search_fields = ('title_one', 'description_one')
  list_per_page = 25


admin.site.register(blog, BlogAdmin)