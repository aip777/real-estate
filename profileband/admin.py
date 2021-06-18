from django.contrib import admin

from .models import Profileband



class ProfilebandAdmin(admin.ModelAdmin):
  list_display = ('id', 'title_one', 'name_one', 'is_published', 'email_address', 'phone_number')
  list_display_links = ('id', 'title_one')
  list_filter = ('name_one',)
  list_editable = ('is_published',)

  search_fields = ('title', 'name_one', 'email_address')
  list_per_page = 25

admin.site.register(Profileband, ProfilebandAdmin)