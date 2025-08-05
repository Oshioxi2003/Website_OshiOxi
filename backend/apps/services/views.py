from rest_framework import generics, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Service, ServiceCategory, ServiceInquiry
from .serializers import (
    ServiceListSerializer, ServiceDetailSerializer,
    ServiceCategorySerializer, ServiceInquirySerializer
)


class ServiceListView(generics.ListAPIView):
    """
    List all active services with filtering and searching
    """
    serializer_class = ServiceListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category__slug', 'is_featured']
    search_fields = ['name', 'short_description', 'description']
    ordering_fields = ['name', 'order', 'created_at']
    ordering = ['order', 'name']

    def get_queryset(self):
        return Service.objects.filter(is_active=True).select_related('category')


class ServiceDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single service by slug
    """
    serializer_class = ServiceDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Service.objects.filter(is_active=True).select_related('category')


class FeaturedServicesView(generics.ListAPIView):
    """
    List featured services
    """
    serializer_class = ServiceListSerializer
    
    def get_queryset(self):
        return Service.objects.filter(
            is_active=True, 
            is_featured=True
        ).select_related('category').order_by('order')


class ServiceCategoryListView(generics.ListAPIView):
    """
    List all service categories
    """
    queryset = ServiceCategory.objects.all()
    serializer_class = ServiceCategorySerializer


class ServiceInquiryCreateView(generics.CreateAPIView):
    """
    Create a new service inquiry
    """
    queryset = ServiceInquiry.objects.all()
    serializer_class = ServiceInquirySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inquiry = serializer.save()
        
        return Response({
            'message': 'Service inquiry submitted successfully. We will contact you soon.',
            'inquiry_id': inquiry.id
        }, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def service_stats(request):
    """
    Get service statistics
    """
    stats = {
        'total_services': Service.objects.filter(is_active=True).count(),
        'total_categories': ServiceCategory.objects.count(),
        'total_inquiries': ServiceInquiry.objects.count(),
        'featured_services': Service.objects.filter(is_active=True, is_featured=True).count()
    }
    return Response(stats)