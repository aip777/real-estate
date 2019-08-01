from django.contrib import admin

from .models import Gallery, Email

class GalleryAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'video', 'is_published', 'gallery_image', 'list_date')
  list_display_links = ('id', 'title')
  list_filter = ('title',)
  list_editable = ('is_published',)

  search_fields = ('title', 'list_date')
  list_per_page = 25



admin.site.register(Gallery, GalleryAdmin)






class EmailAdmin(admin.ModelAdmin):
  list_display = ('id', 'email_name', 'from_email', 'phone', 'message', 'document')
  list_display_links = ('id', 'email_name')
  search_fields = ('email_name', 'from_email', 'phone', )
  list_per_page = 25

  def has_add_permission(self, request):
    return False


  def has_delete_permission(self, request, obj=None):
    return False

admin.site.register(Email, EmailAdmin)