from django.contrib import admin

# Register your models here.
from .models import CsvUpload

# admin.site.register(Member)
# admin.site.register(Document)
# admin.site.register(Ajax)
# admin.site.register(CsvUpload)



class CsvAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'description', 'end_date', 'notes', 'images')
  list_display_links = ('id', 'name')
  list_filter = ('name',)

  search_fields = ('id', 'name', 'description', 'end_date', 'notes')
  list_per_page = 25



admin.site.register(CsvUpload, CsvAdmin)