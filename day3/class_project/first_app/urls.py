from django.conf.urls import url
from first_app import views


urlpatterns = [
         url(r'^$', views.dashboard, name='dashboard'),
         url(r'^enquiries/', views.enquiries, name='enquiries'),
         ]
