from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Blog posts
    path('posts/', views.BlogPostListView.as_view(), name='post_list'),
    path('posts/<slug:slug>/', views.BlogPostDetailView.as_view(), name='post_detail'),
    path('posts/featured/', views.FeaturedPostsView.as_view(), name='featured_posts'),
    path('posts/popular/', views.PopularPostsView.as_view(), name='popular_posts'),
    path('posts/recent/', views.RecentPostsView.as_view(), name='recent_posts'),
    
    # Categories and Tags
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
    path('tags/', views.TagListView.as_view(), name='tag_list'),
    
    # Comments
    path('comments/', views.CommentCreateView.as_view(), name='comment_create'),
    
    # Statistics
    path('stats/', views.blog_stats, name='blog_stats'),
]