from django.conf.urls import url
from django.contrib.auth.views import login, logout
from backend_app import views

app_name = 'backend_app'
urlpatterns = [
    url(r'^$', login, {'template_name':'backend/login.html'}),
    url(r'^logout/$', logout, {'template_name':'backend/logout.html'}),
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^register/$', views.create_user, name='create_user'),
    url(r'^profile_page/$', views.view_profile, name='view_profile'),
    url(r'^edit_page/$', views.edit_profile, name='edit_profile')

]
