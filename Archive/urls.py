from django.conf.urls import url, patterns
from Archive import views

urlpatterns = [


    url('^$', views.home, name="level_one"),
    url('^first', views.level_one, name="level_one"),
    url('^second', views.level_two, name="level_two"),
    url('^third', views.level_three, name="level_three"),
]
