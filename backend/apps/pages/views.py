from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Page, Testimonial, TeamMember, PricingPlan
from .serializers import (
    PageSerializer, PageListSerializer, TestimonialSerializer,
    TeamMemberSerializer, PricingPlanSerializer
)


class PageListView(generics.ListAPIView):
    """
    List all published pages
    """
    serializer_class = PageListSerializer
    
    def get_queryset(self):
        return Page.objects.filter(is_published=True)


class PageDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single page by slug
    """
    serializer_class = PageSerializer
    lookup_field = 'slug'
    
    def get_queryset(self):
        return Page.objects.filter(is_published=True)


class MenuPagesView(generics.ListAPIView):
    """
    List pages that should appear in menu
    """
    serializer_class = PageListSerializer
    
    def get_queryset(self):
        return Page.objects.filter(
            is_published=True, 
            show_in_menu=True
        ).order_by('menu_order')


class TestimonialListView(generics.ListAPIView):
    """
    List all active testimonials
    """
    serializer_class = TestimonialSerializer
    
    def get_queryset(self):
        return Testimonial.objects.filter(is_active=True)


class FeaturedTestimonialsView(generics.ListAPIView):
    """
    List featured testimonials
    """
    serializer_class = TestimonialSerializer
    
    def get_queryset(self):
        return Testimonial.objects.filter(
            is_active=True, 
            is_featured=True
        )


class TeamMemberListView(generics.ListAPIView):
    """
    List all active team members
    """
    serializer_class = TeamMemberSerializer
    
    def get_queryset(self):
        return TeamMember.objects.filter(is_active=True)


class PricingPlanListView(generics.ListAPIView):
    """
    List all active pricing plans
    """
    serializer_class = PricingPlanSerializer
    
    def get_queryset(self):
        return PricingPlan.objects.filter(is_active=True)


@api_view(['GET'])
def site_stats(request):
    """
    Get general site statistics
    """
    stats = {
        'total_pages': Page.objects.filter(is_published=True).count(),
        'total_testimonials': Testimonial.objects.filter(is_active=True).count(),
        'team_members': TeamMember.objects.filter(is_active=True).count(),
        'pricing_plans': PricingPlan.objects.filter(is_active=True).count()
    }
    return Response(stats)