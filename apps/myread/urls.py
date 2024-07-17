# We need always the path

from django.urls import path
from . import views

# .as_view() makes the class callabe
# path('home/', HomePage.as_view(), name='home-page-two')


# Django recognizes path urls when there are
# define in the variable 'urlpatterns'
app_name = 'myread-urls'
urlpatterns = [
    path('', views.home_page, name='home-page')
    ]
