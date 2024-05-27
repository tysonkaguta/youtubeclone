from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('video/<str:pk>', views.video, name='video'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('logout',views.logout, name='logout'),
    path('upload_profile_pic', views.upload_profile_pic, name='upload_profile_pic')
]