from django.conf.urls import url

from .views import home, reservations


app_name = 'core'

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^reservations', reservations, name='reservations'),
]
