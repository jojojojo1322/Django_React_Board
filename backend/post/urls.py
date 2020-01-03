#backend/post/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListPost.as_view()),
    path('<int:pk>/', views.DetailPost.as_view()),
    path('<int:pk>/comment/', views.CommentList.as_view()),
    path('<int:post_pk>/comment/<int:comment_pk>', views.CommentDetail.as_view()),
]