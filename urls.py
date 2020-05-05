from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^calendar/create/$', views.create_calendar, name="calendar_create"),
    url(r'^event/get/$', views.get_event, name="get_event"),
    url(r'^event/create/$', views.create_event, name="create_event"),

]