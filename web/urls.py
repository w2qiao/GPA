from django.conf.urls import *
import  views 

urlpatterns = patterns('',
    ('^$', views.main),
    ('^result/$',views.result)
)