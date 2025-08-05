from rest_framework import serializers
from django.contrib.auth.models import User
from .models import BlogPost, Category, Tag, Comment


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']


class CategorySerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description', 'posts_count']

    def get_posts_count(self, obj):
        return obj.posts.filter(status='published').count()


class TagSerializer(serializers.ModelSerializer):
    posts_count = serializers.SerializerMethodField()

    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug', 'posts_count']

    def get_posts_count(self, obj):
        return obj.posts.filter(status='published').count()


class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'name', 'email', 'website', 'content', 'created_at', 'replies']
        extra_kwargs = {
            'email': {'write_only': True}
        }

    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.filter(is_approved=True), many=True).data
        return []


class BlogPostListSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    reading_time = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'author', 'category', 'tags',
            'excerpt', 'featured_image', 'is_featured', 'views_count',
            'comments_count', 'reading_time', 'created_at', 'published_at'
        ]

    def get_comments_count(self, obj):
        return obj.comments.filter(is_approved=True).count()

    def get_reading_time(self, obj):
        # Estimate reading time (assuming 200 words per minute)
        word_count = len(obj.content.split())
        reading_time = max(1, word_count // 200)
        return reading_time


class BlogPostDetailSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    reading_time = serializers.SerializerMethodField()
    related_posts = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = [
            'id', 'title', 'slug', 'author', 'category', 'tags',
            'excerpt', 'content', 'featured_image', 'is_featured',
            'views_count', 'comments', 'comments_count', 'reading_time',
            'related_posts', 'meta_title', 'meta_description',
            'created_at', 'updated_at', 'published_at'
        ]

    def get_comments(self, obj):
        # Only return top-level approved comments
        comments = obj.comments.filter(is_approved=True, parent=None)
        return CommentSerializer(comments, many=True).data

    def get_comments_count(self, obj):
        return obj.comments.filter(is_approved=True).count()

    def get_reading_time(self, obj):
        word_count = len(obj.content.split())
        reading_time = max(1, word_count // 200)
        return reading_time

    def get_related_posts(self, obj):
        # Get related posts from the same category
        related = BlogPost.objects.filter(
            category=obj.category,
            status='published'
        ).exclude(id=obj.id)[:3]
        
        return BlogPostListSerializer(related, many=True).data


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'website', 'content', 'parent']

    def create(self, validated_data):
        comment = Comment.objects.create(**validated_data)
        return comment