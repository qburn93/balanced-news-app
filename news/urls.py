from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.NewsPostDetail.as_view(), name='news_detail'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='post_like'),
    
]