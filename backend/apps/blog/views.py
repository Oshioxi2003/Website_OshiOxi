from rest_framework import generics, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q, F
from .models import BlogPost, Category, Tag, Comment
from .serializers import (
    BlogPostListSerializer, BlogPostDetailSerializer, 
    CategorySerializer, TagSerializer, CommentCreateSerializer
)


class BlogPostListView(generics.ListAPIView):
    """
    List all published blog posts with filtering, searching, and pagination
    """
    serializer_class = BlogPostListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category__slug', 'tags__slug', 'is_featured']
    search_fields = ['title', 'excerpt', 'content']
    ordering_fields = ['created_at', 'views_count', 'title']
    ordering = ['-created_at']

    def get_queryset(self):
        return BlogPost.objects.filter(status='published').select_related(
            'author', 'category'
        ).prefetch_related('tags')


class BlogPostDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single blog post by slug
    """
    serializer_class = BlogPostDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return BlogPost.objects.filter(status='published').select_related(
            'author', 'category'
        ).prefetch_related('tags', 'comments')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        # Increment views count
        BlogPost.objects.filter(pk=instance.pk).update(views_count=F('views_count') + 1)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class FeaturedPostsView(generics.ListAPIView):
    """
    List featured blog posts
    """
    serializer_class = BlogPostListSerializer
    
    def get_queryset(self):
        return BlogPost.objects.filter(
            status='published', 
            is_featured=True
        ).select_related('author', 'category').prefetch_related('tags')[:6]


class PopularPostsView(generics.ListAPIView):
    """
    List popular blog posts (by views)
    """
    serializer_class = BlogPostListSerializer
    
    def get_queryset(self):
        return BlogPost.objects.filter(status='published').select_related(
            'author', 'category'
        ).prefetch_related('tags').order_by('-views_count')[:10]


class RecentPostsView(generics.ListAPIView):
    """
    List recent blog posts
    """
    serializer_class = BlogPostListSerializer
    
    def get_queryset(self):
        return BlogPost.objects.filter(status='published').select_related(
            'author', 'category'
        ).prefetch_related('tags').order_by('-created_at')[:10]


class CategoryListView(generics.ListAPIView):
    """
    List all blog categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TagListView(generics.ListAPIView):
    """
    List all blog tags
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentCreateView(generics.CreateAPIView):
    """
    Create a new comment
    """
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        comment = serializer.save()
        
        return Response({
            'message': 'Comment submitted successfully. It will be published after review.',
            'comment_id': comment.id
        }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def blog_stats(request):
    """
    Get blog statistics
    """
    stats = {
        'total_posts': BlogPost.objects.filter(status='published').count(),
        'total_categories': Category.objects.count(),
        'total_tags': Tag.objects.count(),
        'total_views': sum(BlogPost.objects.filter(status='published').values_list('views_count', flat=True))
    }
    return Response(stats)