from django.contrib import admin
from .models import ServiceCategory, Service, ServiceInquiry


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'services_count', 'created_at']
    list_filter = ['created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}

    def services_count(self, obj):
        return obj.services.count()
    services_count.short_description = 'Services Count'


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'category', 'starting_price', 'is_active', 
        'is_featured', 'order', 'created_at'
    ]
    list_filter = ['is_active', 'is_featured', 'category', 'created_at']
    search_fields = ['name', 'short_description', 'description']
    readonly_fields = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['order', 'is_active', 'is_featured']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'slug', 'category', 'short_description', 'description')
        }),
        ('Media', {
            'fields': ('featured_image', 'icon')
        }),
        ('Features & Pricing', {
            'fields': ('features', 'starting_price', 'price_description')
        }),
        ('Settings', {
            'fields': ('is_active', 'is_featured', 'order')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('category')


@admin.register(ServiceInquiry)
class ServiceInquiryAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'service', 'email', 'phone', 'status', 'created_at'
    ]
    list_filter = ['status', 'service', 'created_at']
    search_fields = ['name', 'email', 'company', 'service__name']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['status']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone', 'company')
        }),
        ('Service Details', {
            'fields': ('service', 'message', 'budget_range', 'timeline')
        }),
        ('Management', {
            'fields': ('status', 'notes')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('service')