from django.contrib import admin
from .models import Page, Testimonial, TeamMember, PricingPlan


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'template', 'is_published', 'show_in_menu', 'menu_order', 'created_at']
    list_filter = ['is_published', 'show_in_menu', 'template', 'created_at']
    search_fields = ['title', 'content', 'excerpt']
    readonly_fields = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['is_published', 'show_in_menu', 'menu_order']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'excerpt', 'content', 'template', 'featured_image')
        }),
        ('Menu Settings', {
            'fields': ('show_in_menu', 'menu_order')
        }),
        ('Publication', {
            'fields': ('is_published',)
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


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'company', 'position', 'rating', 'is_featured', 'is_active', 'order', 'created_at']
    list_filter = ['is_featured', 'is_active', 'rating', 'created_at']
    search_fields = ['name', 'company', 'position', 'content']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_featured', 'is_active', 'order']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'position', 'company', 'avatar')
        }),
        ('Testimonial', {
            'fields': ('content', 'rating')
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_active', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'email', 'is_active', 'order', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'position', 'bio', 'email']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_active', 'order']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'position', 'bio', 'photo')
        }),
        ('Contact & Social', {
            'fields': ('email', 'linkedin', 'twitter', 'github')
        }),
        ('Settings', {
            'fields': ('is_active', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(PricingPlan)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'price_period', 'is_popular', 'is_active', 'order', 'created_at']
    list_filter = ['is_popular', 'is_active', 'price_period', 'created_at']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_popular', 'is_active', 'order']
    
    fieldsets = (
        ('Plan Information', {
            'fields': ('name', 'description', 'price', 'price_period')
        }),
        ('Features', {
            'fields': ('features', 'highlighted_features')
        }),
        ('Call to Action', {
            'fields': ('button_text', 'button_link')
        }),
        ('Settings', {
            'fields': ('is_popular', 'is_active', 'order')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )