from rest_framework import serializers
from .models import Service, ServiceCategory, ServiceInquiry


class ServiceCategorySerializer(serializers.ModelSerializer):
    services_count = serializers.SerializerMethodField()

    class Meta:
        model = ServiceCategory
        fields = ['id', 'name', 'slug', 'description', 'icon', 'services_count']

    def get_services_count(self, obj):
        return obj.services.filter(is_active=True).count()


class ServiceListSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer(read_only=True)

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'slug', 'category', 'short_description',
            'featured_image', 'icon', 'starting_price', 'price_description',
            'is_featured', 'order'
        ]


class ServiceDetailSerializer(serializers.ModelSerializer):
    category = ServiceCategorySerializer(read_only=True)
    related_services = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = [
            'id', 'name', 'slug', 'category', 'short_description', 'description',
            'featured_image', 'icon', 'features', 'starting_price', 'price_description',
            'is_featured', 'meta_title', 'meta_description', 'related_services'
        ]

    def get_related_services(self, obj):
        # Get related services from the same category
        related = Service.objects.filter(
            category=obj.category,
            is_active=True
        ).exclude(id=obj.id)[:3]
        
        return ServiceListSerializer(related, many=True).data


class ServiceInquirySerializer(serializers.ModelSerializer):
    service_name = serializers.CharField(source='service.name', read_only=True)

    class Meta:
        model = ServiceInquiry
        fields = [
            'id', 'service', 'service_name', 'name', 'email', 'phone', 'company',
            'message', 'budget_range', 'timeline', 'created_at'
        ]
        extra_kwargs = {
            'service': {'write_only': True}
        }

    def create(self, validated_data):
        inquiry = ServiceInquiry.objects.create(**validated_data)
        return inquiry