#!/usr/bin/env python
"""
Script to test API endpoints
"""

import requests
import json
from datetime import datetime

BASE_URL = "http://127.0.0.1:8000/api/v1"

def test_endpoint(method, url, data=None, expected_status=200):
    """Test an API endpoint"""
    full_url = f"{BASE_URL}{url}"
    
    print(f"\n{'='*60}")
    print(f"Testing: {method} {url}")
    print(f"{'='*60}")
    
    try:
        if method.upper() == 'GET':
            response = requests.get(full_url)
        elif method.upper() == 'POST':
            response = requests.post(full_url, json=data)
        else:
            print(f"Unsupported method: {method}")
            return False
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == expected_status:
            print("✅ SUCCESS")
            
            # Pretty print JSON response
            try:
                json_data = response.json()
                if isinstance(json_data, dict) and 'results' in json_data:
                    print(f"Results count: {len(json_data['results'])}")
                elif isinstance(json_data, list):
                    print(f"Items count: {len(json_data)}")
                print(f"Response preview: {json.dumps(json_data, indent=2)[:500]}...")
            except:
                print(f"Response: {response.text[:200]}...")
                
        else:
            print(f"❌ FAILED - Expected {expected_status}, got {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ CONNECTION ERROR - Make sure Django server is running")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False
    
    return True

def test_blog_endpoints():
    """Test blog API endpoints"""
    print("\n" + "="*80)
    print("TESTING BLOG ENDPOINTS")
    print("="*80)
    
    endpoints = [
        ('GET', '/blog/posts/'),
        ('GET', '/blog/posts/featured/'),
        ('GET', '/blog/posts/popular/'),
        ('GET', '/blog/posts/recent/'),
        ('GET', '/blog/categories/'),
        ('GET', '/blog/tags/'),
        ('GET', '/blog/stats/'),
    ]
    
    for method, url in endpoints:
        test_endpoint(method, url)

def test_services_endpoints():
    """Test services API endpoints"""
    print("\n" + "="*80)
    print("TESTING SERVICES ENDPOINTS")
    print("="*80)
    
    endpoints = [
        ('GET', '/services/'),
        ('GET', '/services/featured/'),
        ('GET', '/services/categories/'),
        ('GET', '/services/stats/'),
    ]
    
    for method, url in endpoints:
        test_endpoint(method, url)

def test_contact_endpoints():
    """Test contact API endpoints"""
    print("\n" + "="*80)
    print("TESTING CONTACT ENDPOINTS")
    print("="*80)
    
    endpoints = [
        ('GET', '/contact/faq/'),
        ('GET', '/contact/faq/categories/'),
        ('GET', '/contact/stats/'),
    ]
    
    for method, url in endpoints:
        test_endpoint(method, url)
    
    # Test contact form submission
    contact_data = {
        'name': 'Test User',
        'email': 'test@example.com',
        'subject': 'general',
        'message': 'This is a test message from API test script'
    }
    test_endpoint('POST', '/contact/messages/', contact_data, 201)
    
    # Test newsletter subscription
    newsletter_data = {
        'email': 'newsletter@example.com',
        'name': 'Newsletter Subscriber'
    }
    test_endpoint('POST', '/contact/newsletter/', newsletter_data, 201)

def test_pages_endpoints():
    """Test pages API endpoints"""
    print("\n" + "="*80)
    print("TESTING PAGES ENDPOINTS")
    print("="*80)
    
    endpoints = [
        ('GET', '/pages/'),
        ('GET', '/pages/menu/'),
        ('GET', '/pages/testimonials/'),
        ('GET', '/pages/testimonials/featured/'),
        ('GET', '/pages/team/'),
        ('GET', '/pages/pricing/'),
        ('GET', '/pages/stats/'),
    ]
    
    for method, url in endpoints:
        test_endpoint(method, url)

def test_service_inquiry():
    """Test service inquiry submission"""
    print("\n" + "="*80)
    print("TESTING SERVICE INQUIRY")
    print("="*80)
    
    # First get a service ID (assuming we have sample data)
    response = requests.get(f"{BASE_URL}/services/")
    if response.status_code == 200:
        services = response.json()
        if isinstance(services, dict) and 'results' in services:
            services = services['results']
        
        if services:
            service_id = services[0]['id']
            
            inquiry_data = {
                'service': service_id,
                'name': 'Test Client',
                'email': 'client@example.com',
                'phone': '+1234567890',
                'company': 'Test Company',
                'message': 'I am interested in your web development services.',
                'budget_range': '$5000-$10000',
                'timeline': '2-3 months'
            }
            
            test_endpoint('POST', '/services/inquiries/', inquiry_data, 201)
        else:
            print("No services found - create sample data first")
    else:
        print("Could not fetch services")

def main():
    """Run all API tests"""
    print("OSHIOXI BACKEND API TESTING")
    print("="*80)
    print(f"Testing against: {BASE_URL}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Test all endpoints
    test_blog_endpoints()
    test_services_endpoints()
    test_contact_endpoints()
    test_pages_endpoints()
    test_service_inquiry()
    
    print("\n" + "="*80)
    print("API TESTING COMPLETED")
    print("="*80)
    print("\nNote: Make sure Django server is running with sample data loaded")
    print("Run: python run_commands.py all")

if __name__ == '__main__':
    main()