# NADI-VERSE™ Quick Start Guide
# ==============================

## 1. Install Dependencies
```
pip install -r requirements.txt
```

## 2. Run Database Migrations
```
python manage.py makemigrations
python manage.py migrate
```

## 3. Create Admin Superuser
```
python manage.py createsuperuser
```
Choose username, email, and password for the Django admin panel.

## 4. Start the Development Server
```
python manage.py runserver
```

## 5. Access the Site
- **Main Website:** http://127.0.0.1:8000/
- **Interactive Demo:** http://127.0.0.1:8000/demo/
- **Django Admin:** http://127.0.0.1:8000/admin/

## 6. SSIP Demo Tips
- Open `/admin/` to show live demo submissions to evaluators
- Submit a demo via the form, then refresh admin to show real-time data
- The "NADI-VERSE™" admin panel is styled by Django's default admin

## Project Structure
```
mitu/
├── manage.py
├── requirements.txt
├── db.sqlite3              # auto-created after migrate
├── sattvica_project/       # project config
│   ├── settings.py
│   └── urls.py
├── core/                   # landing page + founder
│   ├── models.py           # FounderProfile
│   ├── views.py
│   └── admin.py
├── demo/                   # interactive dosha demo
│   ├── models.py           # DemoSubmission
│   ├── forms.py
│   ├── utils.py            # generate_dummy_report()
│   ├── views.py
│   └── admin.py
├── templates/
│   ├── base.html
│   ├── partials/_disclaimer.html
│   ├── core/landing.html
│   └── demo/
│       ├── demo.html
│       └── results.html
└── static/
    ├── css/main.css
    └── js/
        ├── main.js
        └── demo.js
```
