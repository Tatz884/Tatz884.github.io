from fastapi import FastAPI

from api.routers import task, done, user, healthcheck

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*"
    # "http://localhost",
    # "http://localhost:8000",
    # "http://localhost:8080",
    # "http://localhost:5000",
    # "http://localhost:5000/*",
    # "https://localhost:5000",
    # "https://localhost:5000/*",
    # "http://0.0.0.0:8080",
    # "http://0.0.0.0:8000",
    # "http://0.0.0.0:5000",
    # "http://0.0.0.0:5000/*",
    # "https://0.0.0.0:5000",
    # "https://0.0.0.0:5000/*",
    # "https://example.org",
    # "https://tatz884.github.io",
    # "https://tatz884.github.io/*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(task.router)
app.include_router(user.router)
app.include_router(healthcheck.router)
# app.include_router(done.router)