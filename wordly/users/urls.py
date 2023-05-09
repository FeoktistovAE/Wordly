from django.urls import path
from wordly.users import views


urlpatterns = [
    path('', views.UsersIndexView.as_view()),
    path('create/', views.UserCreateView.as_view()),
]