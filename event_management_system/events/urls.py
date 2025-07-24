from django.urls import path
from . import views

urlpatterns = [
    # Homepage - Event listing
    path('', views.event_list, name='event_list'),
    path('create/', views.create_event, name='create_event'),
    path('<int:event_id>/', views.event_detail, name='event_detail'),
    path('<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('<int:event_id>/register/', views.register_for_event, name='register_for_event'),
    path('<int:event_id>/unregister/', views.unregister_event, name='unregister_event'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('my-events/', views.my_registered_events, name='my_events'),
    path('logout/', views.logout_view, name='logout'),
]