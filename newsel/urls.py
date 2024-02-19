from django.urls import path,include
from . import views

app_name="newsel"
urlpatterns=[
#  path('',views.extract_news,name="post-list"),
#  path('crawl_web/',views.extract_news,name="post-list"),
 path('api/v1/',include('newsel.api.v1.urls')),
 

 ]