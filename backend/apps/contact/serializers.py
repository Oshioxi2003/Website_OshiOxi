from rest_framework import serializers
from .models import ContactMessage, Newsletter, FAQ


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            'name', 'email', 'phone', 'company', 'subject', 'message'
        ]

    def create(self, validated_data):
        # Get client IP and user agent from request context
        request = self.context.get('request')
        if request:
            validated_data['ip_address'] = self.get_client_ip(request)
            validated_data['user_agent'] = request.META.get('HTTP_USER_AGENT', '')
        
        return ContactMessage.objects.create(**validated_data)

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


class NewsletterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ['email', 'name']

    def create(self, validated_data):
        newsletter, created = Newsletter.objects.get_or_create(
            email=validated_data['email'],
            defaults=validated_data
        )
        if not created:
            # If email already exists, update the name if provided
            if validated_data.get('name'):
                newsletter.name = validated_data['name']
                newsletter.save()
        return newsletter


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'category', 'order']