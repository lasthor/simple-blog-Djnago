from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('profile/',views.profile,name="profile"),
    path('friends_suggestions/',views.friends_suggestions,name="friends_suggestions"),
    path('friends_suggestions/follow/',views.follow,name="follow")
    
]
