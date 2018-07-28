from django.urls import path
from wop import views

urlpatterns = [
    # path('', views.screen_setup_list_view, name='index'),
    path('config/', views.config_view, name='config'),
    path('', views.screen_setup_list_view, name='screen_setup_list'),
    path('screen_setup/<int:screen_setup_id>/', views.screen_setup_detail_view, name='screen_setup_detail'),
    path('screen/<int:screen_id>/', views.screen_detail_view, name='screen_detail'),
    path('image_repo/', views.repo_list_view, name='image_repo_list'),
    path('image_repo/<int:image_repo_id>/', views.image_repo_detail_view, name='image_repo_detail'),
]
