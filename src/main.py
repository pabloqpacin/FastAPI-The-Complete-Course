from fastapi import FastAPI

from database import engine
import models
from routers import auth, admin, users, todos


app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# API healthcheck endpoint
@app.get("/healthy")
def health_check():
    return {'status': 'Healthy'}

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(users.router)
app.include_router(todos.router)

# ---
