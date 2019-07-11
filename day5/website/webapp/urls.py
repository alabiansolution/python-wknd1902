from django.conf.urls import url
from webapp import views


urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^back', views.back_office, name='back_office'),
    url(r'^view', views.view_data, name='view_data'),
    url(r'^add', views.add_data, name='add_data'),
]
