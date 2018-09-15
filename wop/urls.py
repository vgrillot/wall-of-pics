from django.urls import path
from wop import views

urlpatterns = [
    # path('', views.screen_setup_list_view, name='index'),
    path('', views.config_view, name='home'),

    path('config/', views.config_view, name='config'),

    path('screen_setup/', views.screen_setup_list_view, name='screen_setup_list'),
    path('screen_setup/<int:screen_setup_id>/', views.screen_setup_detail_view, name='screen_setup_detail'),

    path('screen/<int:screen_id>/', views.screen_detail_view, name='screen_detail'),

    path('wall/', views.wall_list_view, name='wall_list'),
    path('wall/<int:wall_id>/', views.wall_detail_view, name='wall_detail'),
    path('wall/<int:wall_id>/action', views.wall_action_view, name='wall_action'),

    path('image_repo/', views.repo_list_view, name='image_repo_list'),
    path('image_repo/<int:image_repo_id>/', views.image_repo_detail_view, name='image_repo_detail'),
    path('image_repo/<int:image_repo_id>/scan/', views.image_repo_scan, name='image_repo_scan'),

    path('image/<int:image_id>/', views.image, name='image'),

    path('scr/<int:screen_id>/', views.scr, name='scr'),
    path('img/<str:key>/', views.img, name='img'),

    path('scr/<int:screen_id>/image/', views.scr_next_image, name='scr_next_image'),


]
