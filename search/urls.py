from django.conf.urls import url
from search.views import home, search_by_manufacturer, search_by_name, search_by_salt

urlpatterns = [    
    url(r'^$',home,name='search_home'),
    url(r'^by_name/$', search_by_name, name="search_by_name"),
    url(r'^by_manufacturer/$', search_by_manufacturer,
        name="search_by_manufacturer"),
    url(r'^by_salt/$', search_by_salt, name="search_by_salt"),
]
