from django.urls import path
from . import views


urlpatterns = [
    path('',views.all_users,name='all_users'),
    path('add_friend',views.add_friend,name='add_friend'),
    path('sent_request',views.sent_request,name='sent_request'),
    path('unread_requests_view',views.unread_requests_view,name='unread_requests_view'),
]