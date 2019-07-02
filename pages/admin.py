from django.contrib import admin

from .models import Gallery

class GalleryAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'video', 'is_published', 'gallery_image', 'list_date')
  list_display_links = ('id', 'title')
  list_filter = ('title',)
  list_editable = ('is_published',)

  search_fields = ('title', 'list_date')
  list_per_page = 25



admin.site.register(Gallery, GalleryAdmin)



from .models import Email





admin.site.register(Email)