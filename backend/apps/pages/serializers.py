from rest_framework import serializers
from .models import Page, Testimonial, TeamMember, PricingPlan


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = [
            'id', 'title', 'slug', 'content', 'excerpt', 'template',
            'featured_image', 'meta_title', 'meta_description',
            'created_at', 'updated_at'
        ]


class PageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = [
            'id', 'title', 'slug', 'excerpt', 'template',
            'featured_image', 'created_at'
        ]


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            'id', 'name', 'position', 'company', 'content',
            'avatar', 'rating', 'is_featured'
        ]


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = [
            'id', 'name', 'position', 'bio', 'photo',
            'email', 'linkedin', 'twitter', 'github'
        ]


class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = [
            'id', 'name', 'description', 'price', 'price_period',
            'features', 'highlighted_features', 'is_popular',
            'button_text', 'button_link'
        ]