from fastapi import FastAPI
from app.rest.users.users_routes import user_router


app = FastAPI(title="Arquitetura Hexagonal")

app.include_router(user_router)
