# Image Management System

A full-stack application for managing images with descriptions, built with Django REST Framework and Vue.js.

## Features

- Upload images with descriptions
- View list of all images
- Delete images
- RESTful API
- Modern Vue.js frontend

## Tech Stack

- Backend: Python 3, Django, Django REST Framework
- Frontend: Vue.js
- Database: SQLite (can be configured to use PostgreSQL or MySQL)

## Project Structure

```
paritet/
├── backend/           # Django backend
│   ├── api/          # API endpoints
│   ├── core/         # Core Django settings
│   └── images/       # Image management app
└── frontend/         # Vue.js frontend
    ├── src/          # Source files
    └── public/       # Static files
```

## Setup Instructions

### Backend Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Start the development server:
```bash
npm run serve
```

## API Endpoints

- `POST /api/images/` - Upload image with description
- `GET /api/images/` - Get list of all images
- `DELETE /api/images/<id>/` - Delete image by ID

## License

MIT 