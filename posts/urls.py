from django.conf.urls import url
from .import views

app_name ='posts'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^add/',views.add,name='add'),
    url(r'^view/',views.view,name='view'),    
    url(r'^details/(?P<id>\d+)/$',views.details,name='details'),
    ]
