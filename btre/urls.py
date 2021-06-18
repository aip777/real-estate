
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token

urlpatterns = [
    path('', include('pages.urls')),

    path('', include('sendemail.urls')),


    path('', include('core.urls')),

    path(r'api/auth/jwt/', obtain_jwt_token),
    path(r'api/auth/jwt/refresh/', refresh_jwt_token),
    path(r'api/status/', include('status.api.urls')),
    path(r'api/listings/', include('listings.api.urls')),

    path('blog/', include('blog.urls')),
    path('crudcsv/', include('crudcsv.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

