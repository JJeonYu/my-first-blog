from django.conf.urls import url
#from django.contrib import admin
from bookmark.views import bookmark_list, bookmark_detail 

app_name= 'bookmark'

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^$', bookmark_list, name='index'),
    url(r'^(?P<pk>\d+)/$', bookmark_detail, name='detail'), 
]
