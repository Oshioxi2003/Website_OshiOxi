from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    # Services
    path('', views.ServiceListView.as_view(), name='service_list'),
    path('<slug:slug>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('featured/', views.FeaturedServicesView.as_view(), name='featured_services'),
    
    # Categories
    path('categories/', views.ServiceCategoryListView.as_view(), name='category_list'),
    
    # Inquiries
    path('inquiries/', views.ServiceInquiryCreateView.as_view(), name='inquiry_create'),
    
    # Statistics
    path('stats/', views.service_stats, name='service_stats'),
]