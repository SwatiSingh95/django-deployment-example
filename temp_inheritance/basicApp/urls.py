from django.conf.urls import url 
from . import views

app_name = 'basicApp'

urlpatterns = [
    url(r'^other/',views.other,name='other'),
    url(r'^help/',views.help,name='help'),
]