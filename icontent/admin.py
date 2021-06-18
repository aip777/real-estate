from django.contrib import admin

from .models import Content




class ContentAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'header_email', 'header_phone', 'list_date')
  list_display_links = ('id', 'title')
  list_filter = ('title',)

  search_fields = ('title', 'header_email', 'header_phone')
  list_per_page = 25

  def has_add_permission(self, request):
    return False


  def has_delete_permission(self, request, obj=None):
    return False
admin.site.register(Content, ContentAdmin)