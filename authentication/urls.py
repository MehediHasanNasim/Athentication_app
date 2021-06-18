from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginpage, name="loginpage"),
    path('signup/', views.registerpage, name="registerpage"),
    path('notfound/', views.notfoundpage, name="notfoundpage"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logoutUser, name="logoutUser"),
    path('delete_my_account/', views.delete_my_account, name="delete_my_account"),
]
