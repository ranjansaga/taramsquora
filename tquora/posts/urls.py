from django.conf.urls.defaults import patterns,include,url
from posts import views 
urlpatterns = patterns('',
                            url(r'^home/$',views.home), 
                            url(r'^addquestion/$',views.add_question),
                            url(r'^unansweredquestion/$',views.unanswered_question),
)

