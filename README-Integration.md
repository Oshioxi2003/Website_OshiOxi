# Frontend-Backend Integration Guide

## 🚀 Quick Start

### Option 1: Automatic Start (Windows)
```bash
# Start both backend and frontend together
./start-full-stack.bat
```

### Option 2: Manual Start

#### Start Backend:
```bash
cd backend
python start.py
```

#### Start Frontend:
```bash
cd frontend
npm install
npm run dev
```

## 🔗 Integration Overview

### ✅ Completed Integrations:

#### 1. **API Services Layer**
- **Location**: `frontend/src/services/`
- **Files**: 
  - `api.ts` - Axios client configuration
  - `blogService.ts` - Blog API calls
  - `servicesService.ts` - Services API calls
  - `contactService.ts` - Contact API calls
  - `pagesService.ts` - Pages API calls

#### 2. **Custom Hooks**
- **Location**: `frontend/src/hooks/`
- **Features**:
  - `useApi()` - Generic API hook
  - `useBlogPosts()`, `useFeaturedPosts()` - Blog hooks
  - `useServices()`, `useFeaturedServices()` - Services hooks
  - `useContactSubmission()`, `useNewsletterSubscription()` - Form hooks
  - `usePricingPlans()`, `useTestimonials()` - Pages hooks

#### 3. **TypeScript Types**
- **Location**: `frontend/src/types/api.ts`
- **Coverage**: All API response types defined

#### 4. **Reusable Components**
- `BlogCard` - Dynamic blog post cards
- `PricingCard` - Dynamic pricing plan cards
- `ContactForm` - Contact form with API integration
- `NewsletterForm` - Newsletter subscription form

#### 5. **Updated Components**
- ✅ `BlogArea` - Now fetches real blog posts
- ✅ `PricingAreaHomeOne` - Now fetches real pricing plans
- ✅ Contact forms integrated with backend

## 🌐 API Endpoints Integration

### Blog Endpoints:
- `GET /api/v1/blog/posts/` ✅
- `GET /api/v1/blog/posts/featured/` ✅
- `GET /api/v1/blog/categories/` ✅
- `POST /api/v1/blog/comments/` ✅

### Services Endpoints:
- `GET /api/v1/services/` ✅
- `GET /api/v1/services/featured/` ✅
- `POST /api/v1/services/inquiries/` ✅

### Contact Endpoints:
- `POST /api/v1/contact/messages/` ✅
- `POST /api/v1/contact/newsletter/` ✅
- `GET /api/v1/contact/faq/` ✅

### Pages Endpoints:
- `GET /api/v1/pages/pricing/` ✅
- `GET /api/v1/pages/testimonials/` ✅
- `GET /api/v1/pages/team/` ✅

## 🧪 Testing Integration

### 1. Test Blog Integration:
- Visit: `http://localhost:5173/`
- Check if blog posts load from backend
- Try clicking on blog post links

### 2. Test Pricing Integration:
- Visit: `http://localhost:5173/`
- Scroll to pricing section
- Verify pricing plans load from backend

### 3. Test Contact Form:
- Visit: `http://localhost:5173/contact`
- Fill and submit contact form
- Check Django admin for submitted messages

### 4. Test Newsletter:
- Find newsletter form on any page
- Submit email subscription
- Check Django admin for subscriptions

## 🛠️ Development Workflow

### Adding New API Integration:

1. **Add API endpoint to backend** (already done)
2. **Add TypeScript types** in `frontend/src/types/api.ts`
3. **Add service function** in appropriate service file
4. **Create custom hook** in `frontend/src/hooks/`
5. **Update component** to use the hook
6. **Test integration**

### Example: Adding Testimonials to Home Page:

```typescript
// 1. In component
import { useFeaturedTestimonials } from '../../hooks';

const TestimonialSection = () => {
  const { data: testimonials, loading, error } = useFeaturedTestimonials();
  
  if (loading) return <LoadingSpinner />;
  if (error) return <ErrorMessage error={error} />;
  
  return (
    <div>
      {testimonials?.map(testimonial => (
        <TestimonialCard key={testimonial.id} testimonial={testimonial} />
      ))}
    </div>
  );
};
```

## 🔧 Configuration

### API Base URL:
- Development: `http://127.0.0.1:8000/api/v1`
- Production: Update in `frontend/src/config/api.ts`

### CORS Configuration:
Backend is configured to allow requests from:
- `http://localhost:3000`
- `http://localhost:5173`
- `http://127.0.0.1:3000`
- `http://127.0.0.1:5173`

## 📋 Next Steps to Complete:

### Still Need Integration:
1. **Service Details Page** - Dynamic service pages
2. **Blog Details Page** - Dynamic blog post pages
3. **Team Section** - Team members from API
4. **FAQ Page** - FAQ from backend
5. **Testimonial Components** - More testimonial integrations

### To integrate a new component:
```typescript
// Template for new integration
import { useApiHook } from '../hooks';

const YourComponent = () => {
  const { data, loading, error } = useApiHook();
  
  if (loading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;
  
  return (
    <div>
      {data?.map(item => (
        <div key={item.id}>{item.name}</div>
      ))}
    </div>
  );
};
```

## 🚨 Troubleshooting

### Common Issues:

1. **CORS Errors**: Make sure backend is running on port 8000
2. **404 Errors**: Check API endpoint URLs in `config/api.ts`
3. **Loading States**: All components have loading/error handling
4. **Data Not Showing**: Check Django admin for sample data

### Debug Steps:
1. Check browser Network tab for API calls
2. Verify backend is running: `http://127.0.0.1:8000/api/v1/`
3. Check Django admin: `http://127.0.0.1:8000/admin/`
4. Review console errors in browser DevTools

## ✅ Success Indicators:

- ✅ Frontend loads without errors
- ✅ API calls return data (check Network tab)
- ✅ Components show real data from backend
- ✅ Forms submit successfully
- ✅ Loading states work correctly
- ✅ Error handling displays properly

The integration is working when you see real data from Django admin appearing in your React components!