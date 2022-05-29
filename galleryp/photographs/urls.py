# from django.conf.urls import url
# from django.urls import re_path as url
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('search/', views.search_results, name='search_results'),
    path('category/<category_id>', views.get_category, name='get_category'),
    path('location/<location_id>', views.get_location, name='get_location')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)    
