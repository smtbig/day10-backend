# 📦 Day10 Backend Project

A learning project built with FastAPI, SQLAlchemy, and PostgreSQL, including user authentication, task management, and blog post features.

---

## 🚀 Features

- ✅ User management (register users, list users)  
- ✅ Task management (assign tasks to users, mark complete/incomplete)  
- ✅ Blog post creation (tied to users)  
- ✅ SQLAlchemy ORM models  
- ✅ FastAPI endpoints with async support  
- ✅ Environment configuration via `.env`  
- ✅ PostgreSQL schema and seed data ready-to-go  

---

## 📂 Tech Stack

- **Backend:** FastAPI, Python 3.11+  
- **ORM:** SQLAlchemy (async)  
- **Database:** PostgreSQL  
- **Environment:** python-dotenv  
- **Migrations (optional):** Alembic (not enabled by default)  

---

## ⚙️ Local Setup

1. **Clone the repo**
    ```bash
    git clone https://github.com/your-username/day10-backend.git
    cd day10-backend
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    # On Linux/macOS:
    source venv/bin/activate
    # On Windows:
    venv\Scripts\activate
    ```

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up `.env`**  
   Create a `.env` file in the project root with:
    ```
    DATABASE_URL=postgresql://postgres:YourPasswordHere@localhost:5432/day10_backend
    ```
   Replace `YourPasswordHere` with your actual PostgreSQL password.

---

## 🧱 Set Up the Database

1. **Create the database**
    ```bash
    createdb day10_backend
    ```

2. **Run schema + seed data**
    ```bash
    psql -U postgres -d day10_backend -f init_db.sql
    ```

If no errors appear, your database is ready with:

- ✅ 3 tables: `users`, `tasks`, `blog_posts`  
- ✅ 20 users, 60 tasks, 40 blog posts  

---

## ▶️ Run the App

```bash
uvicorn app.main:app --reload
```

Visit http://localhost:8000/docs to view the interactive Swagger API documentation.

## 📁 Project Structure
```
.
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── crud.py
│   └── routers/
│       ├── users.py
│       ├── tasks.py
│       └── blog_posts.py
├── init_db.sql
├── .env
├── requirements.txt
└── README.md
```

## 🧪 Sample Endpoints

Method -	Endpoint -	Description
GET	- /users/ -	List all users
POST	- /tasks/	- Create new task
GET	- /blog-posts/	- Get all blog posts
...	...	...

## 📘 Notes

This is a beginner-friendly project; database migrations (Alembic) are optional.

Alembic can be added later if needed — instructions available in the docs.

## 📤 Deployment Ready?

If deploying (Railway, Render, Heroku, etc.):

✅ Use PostgreSQL in the cloud

✅ Push init_db.sql and .env.example (but never your real .env)

✅ Add deployment instructions here as needed

## 🧑‍💻 Author

Vasily Z.

[GitHub](https://github.com/smtbig)