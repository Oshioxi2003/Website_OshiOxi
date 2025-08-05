#!/usr/bin/env python
"""
Utility script to run common Django commands
"""

import os
import sys
import subprocess


def run_command(command):
    """Execute a command and print the result"""
    print(f"\n{'='*50}")
    print(f"Running: {command}")
    print(f"{'='*50}")
    
    result = subprocess.run(command, shell=True, capture_output=False)
    if result.returncode != 0:
        print(f"Error: Command failed with return code {result.returncode}")
        return False
    return True


def setup_database():
    """Setup database with migrations"""
    print("Setting up database...")
    
    commands = [
        "python manage.py makemigrations",
        "python manage.py migrate",
    ]
    
    for cmd in commands:
        if not run_command(cmd):
            return False
    
    print("\n✅ Database setup completed!")
    return True


def create_superuser():
    """Create a superuser"""
    print("Creating superuser...")
    if not run_command("python manage.py createsuperuser"):
        return False
    print("\n✅ Superuser created!")
    return True


def load_sample_data():
    """Load sample data"""
    print("Loading sample data...")
    
    # Create sample data script
    sample_data_script = """
from django.contrib.auth.models import User
from apps.blog.models import Category, Tag, BlogPost
from apps.services.models import ServiceCategory, Service
from apps.contact.models import FAQ
from apps.pages.models import Page, Testimonial, TeamMember, PricingPlan

# Create blog categories
tech_cat, _ = Category.objects.get_or_create(name="Technology", defaults={'description': 'Tech related posts'})
business_cat, _ = Category.objects.get_or_create(name="Business", defaults={'description': 'Business related posts'})

# Create blog tags
django_tag, _ = Tag.objects.get_or_create(name="Django")
react_tag, _ = Tag.objects.get_or_create(name="React")
web_tag, _ = Tag.objects.get_or_create(name="Web Development")

# Create service categories
web_service_cat, _ = ServiceCategory.objects.get_or_create(
    name="Web Development",
    defaults={'description': 'Custom web development services', 'icon': 'fas fa-code'}
)

# Create services
web_service, _ = Service.objects.get_or_create(
    name="Custom Web Development",
    defaults={
        'category': web_service_cat,
        'short_description': 'We build custom web applications tailored to your needs',
        'description': 'Our team creates responsive, scalable web applications using modern technologies like Django and React.',
        'features': ['Responsive Design', 'SEO Optimized', 'Fast Loading', 'Security Focused'],
        'starting_price': 2000.00,
        'price_description': 'Starting from',
        'is_featured': True
    }
)

# Create FAQs
FAQ.objects.get_or_create(
    question="What technologies do you use?",
    defaults={
        'answer': 'We primarily use Django for backend and React for frontend development.',
        'category': 'Technical',
        'order': 1
    }
)

# Create pages
about_page, _ = Page.objects.get_or_create(
    title="About Us",
    defaults={
        'content': 'We are a team of passionate developers creating amazing web solutions.',
        'excerpt': 'Learn more about our company and team.',
        'template': 'about',
        'is_published': True,
        'show_in_menu': True,
        'menu_order': 1
    }
)

# Create testimonials
Testimonial.objects.get_or_create(
    name="John Doe",
    defaults={
        'position': 'CEO',
        'company': 'Tech Corp',
        'content': 'Outstanding service and quality work. Highly recommended!',
        'rating': 5,
        'is_featured': True
    }
)

# Create team members
TeamMember.objects.get_or_create(
    name="Jane Smith",
    defaults={
        'position': 'Lead Developer',
        'bio': 'Experienced full-stack developer with 8+ years in web development.',
        'email': 'jane@oshioxi.com',
        'linkedin': 'https://linkedin.com/in/janesmith'
    }
)

# Create pricing plans
PricingPlan.objects.get_or_create(
    name="Starter",
    defaults={
        'description': 'Perfect for small projects',
        'price': 999.00,
        'price_period': 'project',
        'features': ['5 Pages', 'Responsive Design', 'Basic SEO', 'Contact Form'],
        'button_text': 'Get Started',
        'order': 1
    }
)

PricingPlan.objects.get_or_create(
    name="Professional",
    defaults={
        'description': 'Ideal for growing businesses',
        'price': 2499.00,
        'price_period': 'project',
        'features': ['15 Pages', 'CMS Integration', 'Advanced SEO', 'Analytics', 'Email Integration'],
        'is_popular': True,
        'button_text': 'Choose Plan',
        'order': 2
    }
)

print("Sample data created successfully!")
"""
    
    # Write sample data script to temporary file
    with open('create_sample_data.py', 'w') as f:
        f.write(sample_data_script)
    
    if not run_command("python manage.py shell < create_sample_data.py"):
        return False
    
    # Clean up
    os.remove('create_sample_data.py')
    
    print("\n✅ Sample data loaded!")
    return True


def run_server():
    """Run development server"""
    print("Starting development server...")
    run_command("python manage.py runserver")


def show_help():
    """Show available commands"""
    print("""
Available commands:
1. setup     - Setup database and run migrations
2. superuser - Create superuser
3. sample    - Load sample data
4. server    - Run development server
5. all       - Run setup, create superuser, and load sample data
6. help      - Show this help

Usage: python run_commands.py <command>
""")


def main():
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == 'setup':
        setup_database()
    elif command == 'superuser':
        create_superuser()
    elif command == 'sample':
        load_sample_data()
    elif command == 'server':
        run_server()
    elif command == 'all':
        if setup_database():
            print("Would you like to create a superuser? (y/n): ", end='')
            if input().lower().startswith('y'):
                create_superuser()
            load_sample_data()
    elif command == 'help':
        show_help()
    else:
        print(f"Unknown command: {command}")
        show_help()


if __name__ == '__main__':
    main()