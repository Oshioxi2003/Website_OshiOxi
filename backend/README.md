# Oshioxi Website Backend

Django REST API backend cho Oshioxi website.

## Cấu trúc dự án

```
backend/
├── oshioxi_backend/          # Django project settings
├── apps/                     # Django applications
│   ├── blog/                # Blog management
│   ├── services/            # Services management  
│   ├── contact/             # Contact & FAQ
│   └── pages/               # Static pages & content
├── requirements.txt         # Python dependencies
├── run_commands.py         # Utility script
└── README.md               # This file
```

## Cài đặt

### 1. Tạo Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 2. Cài đặt Dependencies

```bash
pip install -r requirements.txt
```

### 3. Cấu hình Environment

Tạo file `.env` từ `.env.example`:

```bash
cp .env.example .env
```

Chỉnh sửa các giá trị trong `.env` theo môi trường của bạn.

### 4. Setup Database

```bash
python run_commands.py setup
```

Hoặc chạy từng lệnh:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Tạo Superuser

```bash
python run_commands.py superuser
```

Hoặc:

```bash
python manage.py createsuperuser
```

### 6. Load Sample Data (Optional)

```bash
python run_commands.py sample
```

### 7. Chạy Development Server

```bash
python run_commands.py server
```

Hoặc:

```bash
python manage.py runserver
```

## API Endpoints

### Blog API
- `GET /api/v1/blog/posts/` - Danh sách blog posts
- `GET /api/v1/blog/posts/{slug}/` - Chi tiết blog post
- `GET /api/v1/blog/posts/featured/` - Blog posts nổi bật
- `GET /api/v1/blog/categories/` - Danh sách categories
- `GET /api/v1/blog/tags/` - Danh sách tags
- `POST /api/v1/blog/comments/` - Tạo comment

### Services API
- `GET /api/v1/services/` - Danh sách services
- `GET /api/v1/services/{slug}/` - Chi tiết service
- `GET /api/v1/services/featured/` - Services nổi bật
- `POST /api/v1/services/inquiries/` - Gửi inquiry

### Contact API
- `POST /api/v1/contact/messages/` - Gửi contact message
- `POST /api/v1/contact/newsletter/` - Đăng ký newsletter
- `GET /api/v1/contact/faq/` - Danh sách FAQ

### Pages API
- `GET /api/v1/pages/` - Danh sách pages
- `GET /api/v1/pages/{slug}/` - Chi tiết page
- `GET /api/v1/pages/testimonials/` - Testimonials
- `GET /api/v1/pages/team/` - Team members
- `GET /api/v1/pages/pricing/` - Pricing plans

## Admin Interface

Truy cập Django Admin tại: `http://localhost:8000/admin/`

### Tính năng Admin:
- **Blog Management**: Quản lý posts, categories, tags, comments
- **Services Management**: Quản lý services, categories, inquiries
- **Contact Management**: Quản lý messages, newsletter, FAQ
- **Pages Management**: Quản lý static pages, testimonials, team, pricing

## Models

### Blog App
- `BlogPost`: Blog posts với SEO fields
- `Category`: Blog categories
- `Tag`: Blog tags
- `Comment`: Comments với nested replies

### Services App
- `Service`: Services với features và pricing
- `ServiceCategory`: Service categories
- `ServiceInquiry`: Service inquiries từ clients

### Contact App
- `ContactMessage`: Contact form messages
- `Newsletter`: Newsletter subscriptions
- `FAQ`: Frequently asked questions

### Pages App
- `Page`: Static pages với templates
- `Testimonial`: Customer testimonials
- `TeamMember`: Team member profiles
- `PricingPlan`: Pricing plans

## Tính năng

### Blog System
- ✅ Full blog functionality với categories và tags
- ✅ Comments system với nested replies
- ✅ SEO optimization
- ✅ Featured posts
- ✅ View counting

### Services Management
- ✅ Service catalog với categories
- ✅ Service inquiries
- ✅ Flexible pricing system
- ✅ Features listing

### Contact System
- ✅ Contact form với email notifications
- ✅ Newsletter subscription
- ✅ FAQ management
- ✅ Admin interface để quản lý

### Content Management
- ✅ Dynamic pages
- ✅ Testimonials management
- ✅ Team profiles
- ✅ Pricing plans

### API Features
- ✅ Django REST Framework
- ✅ Filtering, searching, pagination
- ✅ CORS support cho frontend
- ✅ Comprehensive serializers

## Development

### Chạy Tests

```bash
python manage.py test
```

### Tạo Migration

```bash
python manage.py makemigrations
python manage.py migrate
```

### Shell Access

```bash
python manage.py shell
```

### Collect Static Files

```bash
python manage.py collectstatic
```

## Production Deployment

### Environment Variables
Đảm bảo set các environment variables sau cho production:

```bash
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:pass@localhost/dbname
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Database
Khuyến nghị sử dụng PostgreSQL cho production.

### Static Files
Cấu hình web server (nginx/apache) để serve static files.

## Support

Nếu gặp vấn đề, vui lòng tạo issue hoặc liên hệ team development.