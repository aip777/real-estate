from django.contrib import admin

from .models import Content




class ContentAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'header_email', 'header_phone', 'list_date')
  list_display_links = ('id', 'title')
  list_filter = ('title',)

  search_fields = ('title', 'header_email', 'header_phone')
  list_per_page = 25

admin.site.register(Content, ContentAdmin)