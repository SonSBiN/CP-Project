from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
    path('chatroom/', views.index),
    path('create_post/', views.PostCreate.as_view()),
]
