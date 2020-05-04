from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^calendar/create/$', views.create_calendar, name="calendar_create"),

]