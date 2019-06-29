from django.conf.urls import url
from App_Two import views


urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^add', views.add_post, name='add_post'),
    url(r'^del', views.del_post, name='del_post'),
]
