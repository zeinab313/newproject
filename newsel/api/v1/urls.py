from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

app_name="api-v1"

# router=DefaultRouter()
# router.register('crawl_web',views.NewsViewset,basename='post-list')
# # router.register('crawl_web',views.NewsModelViewset,basename='post-list')
# urlpatterns=router.urls

urlpatterns=[
#  path('crawl_web/<int:pk>/',views.NewsViewset.as_view({'get':'list'}),name="crawl_web"),
 path('crawl_web/',views.NewsViewset.as_view({'get':'list'}),name="crawl_web"),
 path('crawl_search/',views.SearchViewset.as_view({'post':'create'}),name='crawl_search'),
#  path('crawl_search/',views.SearchViewset.as_view({'get':'list'}),name='crawl_search'),
#  path('change-password/', views.ChangePasswordApiView.as_view(), name='change-password'),
 ]