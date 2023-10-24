
from django.contrib import admin
from django.urls import path,include
from agenda.urls import urlpatterns as agenda_urls
 
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',include(agenda_urls)),
]
