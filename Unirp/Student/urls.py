from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name='home'),
    path('Login/',views.loginpage,name='login'),
    path('Register/',views.registeruser,name="register"),
    path('Profile/',views.profilepage,name="profile"),
    path('Attendance/',views.attendancepage,name="attendance"),
    path('Logout/',views.logoutpage,name="logout")
]
