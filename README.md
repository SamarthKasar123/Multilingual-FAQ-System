# Multilingual FAQ System 🌐

A robust Django-based FAQ management system with multi-language support, WYSIWYG editing, and efficient caching. This system allows you to manage FAQs in multiple languages with automatic translation support.

## 🌟 Features

- **Multi-language Support**
  - Automatic translation to Hindi and Bengali
  - Easy addition of new languages
  - Fallback to English when translations are unavailable

- **Rich Text Editing**
  - Integrated CKEditor for WYSIWYG editing
  - Support for formatting, images, and links
  - Multi-language content editing

- **Performance Optimization**
  - Redis-based caching system
  - Efficient API responses
  - Pre-translated content storage

- **API Features**
  - RESTful API endpoints
  - Language selection via query parameters
  - Swagger/ReDoc API documentation

- **Admin Interface**
  - User-friendly admin panel
  - Easy content management
  - Translation status monitoring

## 🚀 Installation

### Prerequisites
- Python 3.9+
- Redis Server
- Git

### Local Development Setup

1. **Clone the Repository**
   ```bash
   git clone <your-repository-url>
   cd multilingual-faq-system
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Setup**
   ```bash
   # Create .env file
   cp .env.example .env
   
   # Generate Django Secret Key and update .env
   python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
   ```

5. **Database Setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. **Start Redis Server**
   ```bash
   # Using Docker
   docker-compose up redis -d
   
   # Or install and run Redis locally
   redis-server
   ```

7. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

### Docker Setup

1. **Build and Run**
   ```bash
   docker-compose up --build
   ```

2. **Create Superuser in Docker**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

## 📚 API Documentation

### Base URL
- Development: `http://localhost:8000/api/`
- Production: `https://your-domain.com/api/`

### Endpoints

#### FAQ Endpoints
- `GET /api/faqs/` - List all FAQs
- `GET /api/faqs/?lang=hi` - Get FAQs in Hindi
- `GET /api/faqs/?lang=bn` - Get FAQs in Bengali
- `POST /api/faqs/` - Create new FAQ
- `PUT /api/faqs/{id}/` - Update FAQ
- `DELETE /api/faqs/{id}/` - Delete FAQ

#### Example Requests

```bash
# Get all FAQs in English
curl http://localhost:8000/api/faqs/

# Get FAQs in Hindi
curl http://localhost:8000/api/faqs/?lang=hi

# Create new FAQ
curl -X POST http://localhost:8000/api/faqs/ \
  -H "Content-Type: application/json" \
  -d '{
    "question": "What is this?",
    "answer": "This is a test FAQ"
  }'
```

## 🛠️ Development

### Project Structure
```
multilingual-faq-system/
├── faq/                    # Main application
│   ├── models.py          # FAQ models
│   ├── serializers.py     # API serializers
│   ├── views.py           # API views
│   ├── admin.py           # Admin interface
│   └── tests.py           # Test cases
├── faq_project/           # Project settings
├── docker/                # Docker configuration
├── requirements.txt       # Python dependencies
└── manage.py             # Django management
```

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=faq
```

### Code Quality
```bash
# Run flake8
flake8 .

# Run black formatter
black .
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file with:
```env
DEBUG=True
DJANGO_SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
REDIS_URL=redis://localhost:6379/1
```

### Redis Configuration
Default configuration in `settings.py`:
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
    }
}
```

## 📈 Performance Optimization

- Redis caching for FAQ responses
- Translation caching
- Database query optimization
- Efficient API pagination

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit your changes
   ```bash
   git commit -m 'feat: Add amazing feature'
   ```
4. Push to the branch
   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the Samarth Kasar file for details.

## 🆘 Support

For support, email samarthkasar9924@gmail.com or open an issue in the repository.

## 🔗 Links

- [API Documentation](http://localhost:8000/swagger/)
- [Admin Interface](http://localhost:8000/admin/)
- [Redis Documentation](https://redis.io/documentation)
- [Django Documentation](https://docs.djangoproject.com/)