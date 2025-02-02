# Multilingual FAQ System

A Django-based FAQ system with multilingual support, WYSIWYG editor, and caching capabilities.

## Features

- Multilingual FAQ management with automatic translation
- Rich text editor support using CKEditor
- Redis-based caching for improved performance
- RESTful API with language selection
- Docker support for easy deployment
- Comprehensive test coverage

## Installation

### Local Development

1. Clone the repository:
```bash
git clone <your-repo-url>
cd multilingual-faq-system
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

### Docker Installation

1. Build and run with Docker Compose:
```bash
docker-compose up --build
```

## API Usage

### Endpoints

- GET `/api/faqs/` - List all FAQs
- GET `/api/faqs/?lang=hi` - List FAQs in Hindi
- GET `/api/faqs/?lang=bn` - List FAQs in Bengali
- POST `/api/faqs/` - Create new FAQ
- PUT `/api/faqs/{id}/` - Update FAQ
- DELETE `/api/faqs/{id}/` - Delete FAQ

### Example API Requests

```bash
# Get FAQs in English
curl http://localhost:8000/api/faqs/

# Get FAQs in Hindi
curl http://localhost:8000/api/faqs/?lang=hi

# Create new FAQ
curl -X POST http://localhost:8000/api/faqs/ \
  -H "Content-Type: application/json" \
  -d '{"question":"What is this?","answer":"This is a test FAQ"}'
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Testing

Run tests using pytest:
```bash
pytest
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.