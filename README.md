# Brno Beer Map 

A web application built with Django and PostgreSQL that allows users to explore Brno pubs, filter them by available beers, and manage their favorite venues and beers.

---
## Features

- View pubs and breweries in Brno
- Filter venues by type of beer
- Register/login/logout functionality
- Add/remove favorite beers and venues
- View personalized profile with favorites
- Admin interface to manage data
- Fully documented models, views, forms, and URLs
- Unit tests with Pytest

---

## Technologies

- Python 3.12
- Django 5.x
- PostgreSQL
- HTML/CSS 
- Pytest

---

## ⚙️ Setup

1. **Clone the repo**  
   `git clone https://github.com/yourusername/brno-beer-map.git`

2. **Create virtual environment**  
   `python -m venv venv && source venv/bin/activate`

3. **Install dependencies**  
   `pip install -r requirements.txt`

4. **Configure PostgreSQL**  
   Create database and user as described in `settings.py`

5. **Run migrations**  
   `python manage.py migrate`

6. **Start the development server**  
   `python manage.py runserver`

7. **Access the app**  
   Visit `http://127.0.0.1:8000/`

---

## Running tests

```bash
pytest
