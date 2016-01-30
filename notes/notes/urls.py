from django.conf.urls import include, url
from django.contrib import admin
from myapp import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'notes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'myapp.views.notes', name='notes'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls')),
]
