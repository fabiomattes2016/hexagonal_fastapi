import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.rest.users.users_routes import user_router, private_user_router
from app.rest.authentication.authentication_routes import auth_router
from app.infrastructure.security import JWTAuth
from starlette.middleware.authentication import AuthenticationMiddleware


logging.getLogger('passlib').setLevel(logging.ERROR)

app = FastAPI(
    title="API's Agencia 0736",
    version="0.1.0",
    summary="Esta api tem por objetivo centralizar todas as API's de cooperativa para uso interno, desenvolvida em python com padrão de arquitetura hexagonal.",
    docs_url="/swagger",
    redoc_url="/docs"
)

app.include_router(user_router)
app.include_router(private_user_router)
app.include_router(auth_router)

# Add middleware
app.add_middleware(AuthenticationMiddleware, backend=JWTAuth())


@app.get('/')
def health_check():
    return JSONResponse(content={'status': 'running'})
