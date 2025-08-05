from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    # Contact messages
    path('messages/', views.ContactMessageCreateView.as_view(), name='message_create'),
    
    # Newsletter
    path('newsletter/', views.NewsletterSubscribeView.as_view(), name='newsletter_subscribe'),
    
    # FAQ
    path('faq/', views.FAQListView.as_view(), name='faq_list'),
    path('faq/categories/', views.faq_categories, name='faq_categories'),
    
    # Statistics
    path('stats/', views.contact_stats, name='contact_stats'),
]