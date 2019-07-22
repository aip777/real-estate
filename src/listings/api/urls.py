from django.conf.urls import url


from .views import (
    # StatusListSearchAPIView,
    ListingAPIView,
    ListingAPIDetailView,
    # StatusCreateAPIView,
    # StatusDetailAPIView,
    # StatusUpdateAPIView,
    # StatusDeleteAPIView,
)
urlpatterns = [
    url(r'^$', ListingAPIView.as_view()),
    url(r'^(?P<id>\d+)/$', ListingAPIDetailView.as_view()),

    # url(r'^create/$', StatusCreateAPIView.as_view()),
    # url(r'(?P<id>\d+)/$', StatusDetailAPIView.as_view()),


    # url(r'^(?P<pk>\d+)/update/$', StatusUpdateAPIView.as_view()),
    # url(r'^(?P<pk>\d+)/delete/$', StatusDeleteAPIView.as_view()),

]