from fastapi import FastAPI
from app.routers import users, tasks, blog

app = FastAPI()

app.include_router(users.router)
app.include_router(tasks.router)
app.include_router(blog.router)

@app.get("/")
def root():
    return {"msg": "Welcome to your real-world backend!"}
