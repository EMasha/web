from django.conf.urls import url
from .views import *

app_name = 'shop'
urlpatterns = [
    url(r'^contact/$', contact, name='contact'),
    url(r'success/', successView, name='success'),
    url(r'error/', errorView, name='error'),
    url(r'^search-results/$', product_query, name='search-results'),
    url(r'^$', product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', product_detail, name='product_detail'),


]