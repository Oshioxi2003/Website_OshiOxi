from django.contrib import admin
from .models import ContactMessage, Newsletter, FAQ


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'email', 'subject', 'status', 'created_at'
    ]
    list_filter = ['status', 'subject', 'created_at']
    search_fields = ['name', 'email', 'company', 'message']
    readonly_fields = ['ip_address', 'user_agent', 'created_at', 'updated_at']
    list_editable = ['status']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone', 'company')
        }),
        ('Message Details', {
            'fields': ('subject', 'message')
        }),
        ('Management', {
            'fields': ('status', 'notes')
        }),
        ('Technical Info', {
            'fields': ('ip_address', 'user_agent'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    actions = ['mark_as_resolved', 'mark_as_spam']

    def mark_as_resolved(self, request, queryset):
        queryset.update(status='resolved')
        self.message_user(request, f'{queryset.count()} messages marked as resolved.')
    mark_as_resolved.short_description = 'Mark selected messages as resolved'

    def mark_as_spam(self, request, queryset):
        queryset.update(status='spam')
        self.message_user(request, f'{queryset.count()} messages marked as spam.')
    mark_as_spam.short_description = 'Mark selected messages as spam'


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'is_active', 'confirmed_at', 'created_at']
    list_filter = ['is_active', 'confirmed_at', 'created_at']
    search_fields = ['email', 'name']
    readonly_fields = ['created_at']
    list_editable = ['is_active']

    actions = ['activate_subscribers', 'deactivate_subscribers']

    def activate_subscribers(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, f'{queryset.count()} subscribers activated.')
    activate_subscribers.short_description = 'Activate selected subscribers'

    def deactivate_subscribers(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, f'{queryset.count()} subscribers deactivated.')
    deactivate_subscribers.short_description = 'Deactivate selected subscribers'


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'order', 'is_active', 'created_at']
    list_filter = ['is_active', 'category', 'created_at']
    search_fields = ['question', 'answer', 'category']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['order', 'is_active']

    fieldsets = (
        ('FAQ Content', {
            'fields': ('question', 'answer', 'category')
        }),
        ('Settings', {
            'fields': ('order', 'is_active')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )