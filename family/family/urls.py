from django.conf.urls import include, url
#from django.contrib import admin
from home_family import views

urlpatterns = [
    # Examples:
    url(r'^$', 'home_family.views.home'),
  
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
]
