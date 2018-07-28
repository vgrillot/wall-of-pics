from django.urls import path
from wop import views

urlpatterns = [
    path('', views.screen_setup_list_view, name='index'),
    path('screen_setup/<int:screen_setup_id>/', views.screen_setup_detail_view, name='screen_setup_detail'),
    path('screen/<int:screen_id>/', views.screen_detail_view, name='screen_detail'),
]
