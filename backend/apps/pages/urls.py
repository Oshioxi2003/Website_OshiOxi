from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    # Pages
    path('', views.PageListView.as_view(), name='page_list'),
    path('<slug:slug>/', views.PageDetailView.as_view(), name='page_detail'),
    path('menu/', views.MenuPagesView.as_view(), name='menu_pages'),
    
    # Testimonials
    path('testimonials/', views.TestimonialListView.as_view(), name='testimonial_list'),
    path('testimonials/featured/', views.FeaturedTestimonialsView.as_view(), name='featured_testimonials'),
    
    # Team
    path('team/', views.TeamMemberListView.as_view(), name='team_list'),
    
    # Pricing
    path('pricing/', views.PricingPlanListView.as_view(), name='pricing_list'),
    
    # Statistics
    path('stats/', views.site_stats, name='site_stats'),
]