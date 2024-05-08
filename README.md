Codemonk Project
================

This project implements a RESTful API using Django Rest Framework for storing and searching paragraphs of text. Users can register, log in, insert paragraphs of text, and search for specific words within the stored paragraphs.

Installation
------------

**Requirements:**
- Python 3.9.11
- Docker (optional, for containerized deployment)
- PostgreSQL database (can be run using Docker)

**Steps:**
1. Clone the repository:
```
git clone https://github.com/Nikunj6265/Text-Extractor.git
cd Text-Extractor
```

3. Set up a virtual environment (optional but recommended):
 ```
python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```
4. Set up environment variables:
- Create a `.env` file in the project root directory.
- Add the following environment variables:
  ```
  DB_NAME=your_database_name
  DB_USER=your_database_user
  DB_PASS=your_database_password
  ```



5. In settings.py file:
   In the DATABASES section change **'HOST':'127.0.0.1'**(If not using docker-compose) 
  ```
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
        'HOST': 'db',  # Assuming your PostgreSQL service is named 'db' in docker-compose
        'PORT': '5432',
    }
}
  ```
7. Run migrations:
```
python manage.py makemigrations
python manage.py migrate
```

6. Start the development server:
```
python manage.py runserver
```

Usage
-----

**User Authentication**

- **Registration:**
- Endpoint: POST /api/register/
- Body: JSON object with email, password, confirm_password, name, and dob.
- **Login:**
- Endpoint: POST /api/login/
- Body: JSON object with email and password.
- **Logout:**
- Endpoint: POST /api/logout/

**User Details**

- **Get User Details:**
- Endpoint: GET /api/update-details/
- Requires authentication.
- **Update User Details:**
- Endpoint: PATCH /api/update-details/
- Body: JSON object with updated name and dob.
- Requires authentication.

**Text Operations**

- **Insert Paragraphs:**
- Endpoint: POST /api/insert-text/
- Body: JSON object with text containing paragraphs separated by two newline characters.
- Requires authentication.
- **Search Word:**
- Endpoint: POST /api/word-search/
- Body: JSON object with word to search within paragraphs.
- Requires authentication.
## Docker Deployment (optional)

1. Build Docker images:
    ```bash
    docker-compose build
    ```

2. Start containers:
    ```bash
    docker-compose up
    ```

3. Access the API:
    - By default, the API can be accessed at [http://0.0.0.0:8000/](http://0.0.0.0:8000/).
    - If you prefer to use `localhost`, you can update the URL by modifying the URL by **[http://localhost:8000/].**
    - After making this change, all the APIs work fine.
