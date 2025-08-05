from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .models import ContactMessage, Newsletter, FAQ
from .serializers import ContactMessageSerializer, NewsletterSerializer, FAQSerializer


class ContactMessageCreateView(generics.CreateAPIView):
    """
    Create a new contact message
    """
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        contact_message = serializer.save()
        
        # Send notification email (optional)
        try:
            self.send_notification_email(contact_message)
        except Exception as e:
            # Log the error but don't fail the request
            print(f"Failed to send notification email: {e}")
        
        return Response({
            'message': 'Your message has been sent successfully. We will get back to you soon.',
            'contact_id': contact_message.id
        }, status=status.HTTP_201_CREATED)

    def send_notification_email(self, contact_message):
        """Send notification email to admin"""
        subject = f'New Contact Message: {contact_message.get_subject_display()}'
        message = f"""
        New contact message received:
        
        Name: {contact_message.name}
        Email: {contact_message.email}
        Phone: {contact_message.phone}
        Company: {contact_message.company}
        Subject: {contact_message.get_subject_display()}
        
        Message:
        {contact_message.message}
        
        Sent at: {contact_message.created_at}
        """
        
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            ['admin@oshioxi.com'],  # Replace with actual admin email
            fail_silently=False,
        )


class NewsletterSubscribeView(generics.CreateAPIView):
    """
    Subscribe to newsletter
    """
    queryset = Newsletter.objects.all()
    serializer_class = NewsletterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        newsletter = serializer.save()
        
        return Response({
            'message': 'Successfully subscribed to newsletter!',
            'email': newsletter.email
        }, status=status.HTTP_201_CREATED)


class FAQListView(generics.ListAPIView):
    """
    List all active FAQs
    """
    serializer_class = FAQSerializer
    
    def get_queryset(self):
        queryset = FAQ.objects.filter(is_active=True)
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category=category)
        return queryset


@api_view(['GET'])
def contact_stats(request):
    """
    Get contact statistics
    """
    stats = {
        'total_messages': ContactMessage.objects.count(),
        'new_messages': ContactMessage.objects.filter(status='new').count(),
        'newsletter_subscribers': Newsletter.objects.filter(is_active=True).count(),
        'total_faqs': FAQ.objects.filter(is_active=True).count()
    }
    return Response(stats)


@api_view(['GET'])
def faq_categories(request):
    """
    Get available FAQ categories
    """
    categories = FAQ.objects.filter(is_active=True).values_list('category', flat=True).distinct()
    categories = [cat for cat in categories if cat]  # Remove empty categories
    return Response({'categories': categories})