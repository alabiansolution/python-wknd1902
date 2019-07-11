from django.conf.urls import url
from myfirst_app import views


urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^add_page/', views.add_post, name='add_post'),
]
