# Restaurant Backend

A Django-based backend system for managing a restaurant, including menus, orders, and admin interface.

---

## Setup Instructions

### 1. Create and Activate Virtual Environment
```bash
git clone https://github.com/yourusername/restaurant-backend.git
cd restaurant-backend
```

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip3 install -r requirements.txt
```

### 4. Apply Migrations
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py load_food_items food_items.json
```

### 5. Create Superuser
```bash
python3 manage.py createsuperuser
```

### 6. Run the Development Server
```bash
python3 manage.py runserver
```
Then visit: http://127.0.0.1:8000/admin/ to log in.
