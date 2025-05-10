# Django Web Scraper

![Python](https://img.shields.io/badge/python-3.x-blue)
![Django](https://img.shields.io/badge/django-5.2-green)
![Bootstrap](https://img.shields.io/badge/bootstrap-4.3-purple)

A simple web scraping application built with Django that extracts links from any website URL you provide.

## Features

- Extract all links from a given webpage
- Clean responsive interface with Bootstrap 4
- Delete all links with one click
- Displays link name, URL and ID

## Screenshot

![Screenshot](screenshot.png)

## Requirements

- Python 3.6+
- Django 5.0
- BeautifulSoup4
- requests

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/django-scraper.git
cd django-scraper
```

2.Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```

3. Install requirements:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start development server:

```bash
python manage.py runserver
```

6. Open http://127.0.0.1:8000 in your browser

## Usage

1. Enter any website URL in the input field
2. Click "Scrape" button
3. View all extracted links in the table
4. Use "Clear All Links" to reset

## Project Structure

```
django-scraper/
├── scraper/ # Main project folder
├── scraper_app/ # Scraper application
│ ├── templates/ # HTML templates
│ ├── models.py # Link model
│ ├── views.py # Scraping logic
├── manage.py
└── requirements.txt
```

## Customization

### To modify the styling:

1. Edit the Bootstrap classes in templates/result.html

2. Or add custom CSS in static/css/styles.css

## License

#### MIT
