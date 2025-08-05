#!/usr/bin/env python
"""
Quick start script for Oshioxi Backend
"""

import os
import sys
import subprocess

def run_command(command, check=True):
    """Run command and handle errors"""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    if check and result.returncode != 0:
        print(f"Error: Command failed")
        return False
    return True

def quick_start():
    """Quick start the backend"""
    print("🚀 Starting Oshioxi Backend...")
    print("="*50)
    
    # Check if we need to run migrations
    if not os.path.exists('db.sqlite3'):
        print("📊 Setting up database...")
        if not run_command("python manage.py makemigrations"):
            return
        if not run_command("python manage.py migrate"):
            return
        print("✅ Database created!")
        
        # Ask if user wants sample data
        print("\n📝 Would you like to create sample data? (y/n): ", end='')
        if input().lower().startswith('y'):
            print("Creating sample data...")
            sample_script = '''
from django.contrib.auth.models import User
from apps.blog.models import Category, Tag, BlogPost
from apps.services.models import ServiceCategory, Service
from apps.contact.models import FAQ
from apps.pages.models import Page, Testimonial, PricingPlan

# Create admin user if not exists
if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "admin@oshioxi.com", "admin123")
    print("Admin user created - username: admin, password: admin123")

# Blog data
tech_cat, _ = Category.objects.get_or_create(name="Technology")
web_tag, _ = Tag.objects.get_or_create(name="Web Development")

if not BlogPost.objects.exists():
    admin_user = User.objects.get(username="admin")
    post = BlogPost.objects.create(
        title="Welcome to Oshioxi Blog",
        author=admin_user,
        category=tech_cat,
        excerpt="This is our first blog post!",
        content="Welcome to our blog where we share insights about web development and technology.",
        status="published",
        is_featured=True
    )
    post.tags.add(web_tag)

# Services data  
web_cat, _ = ServiceCategory.objects.get_or_create(
    name="Web Development",
    defaults={"description": "Custom web solutions", "icon": "fas fa-code"}
)

Service.objects.get_or_create(
    name="Custom Website Development",
    defaults={
        "category": web_cat,
        "short_description": "Professional custom websites",
        "description": "We create amazing websites tailored to your needs",
        "features": ["Responsive Design", "SEO Optimized", "Fast Loading"],
        "starting_price": 1500.00,
        "is_featured": True
    }
)

# FAQ
FAQ.objects.get_or_create(
    question="What services do you offer?",
    defaults={
        "answer": "We offer web development, mobile apps, and digital marketing services",
        "category": "General"
    }
)

# Pages
Page.objects.get_or_create(
    title="About Us",
    defaults={
        "content": "We are a team of passionate developers creating amazing digital solutions.",
        "excerpt": "Learn more about our company",
        "is_published": True
    }
)

# Testimonials
Testimonial.objects.get_or_create(
    name="John Smith",
    defaults={
        "company": "Tech Corp",
        "position": "CEO", 
        "content": "Excellent service and quality work!",
        "rating": 5,
        "is_featured": True
    }
)

# Pricing
PricingPlan.objects.get_or_create(
    name="Starter Package",
    defaults={
        "description": "Perfect for small businesses",
        "price": 999.00,
        "price_period": "project",
        "features": ["5 Pages", "Responsive Design", "Basic SEO"],
        "button_text": "Get Started"
    }
)

print("✅ Sample data created successfully!")
'''
            
            with open('temp_sample.py', 'w') as f:
                f.write(sample_script)
            
            run_command("python manage.py shell < temp_sample.py", check=False)
            os.remove('temp_sample.py')
    
    # Start server
    print("\n🌐 Starting development server...")
    print("Admin: http://127.0.0.1:8000/admin/ (admin/admin123)")
    print("API: http://127.0.0.1:8000/api/v1/")
    print("\nPress Ctrl+C to stop the server")
    run_command("python manage.py runserver", check=False)

if __name__ == '__main__':
    quick_start()