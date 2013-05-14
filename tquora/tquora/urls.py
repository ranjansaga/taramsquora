from django.conf.urls import patterns, include, url
from tquora import settings
from django.conf.urls.static import static
 
urlpatterns = patterns('',
                      url(r'^$','posts.views.home'),
                      url(r'^tquora/',include('posts.urls')),
                    ) 
                                                     

if settings.DEBUG:
        urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$','django.views.static.serve',
                                {'document_root':settings.MEDIA_ROOT,}),
                            )
