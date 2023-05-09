from fastapi import FastAPI
from api import health_check, samples, items, tax, todo
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS設定
origins = [
    "http://localhost",
    "http://localhost:8080",
    # 他の許可するオリジンをここに追加する
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_check.router, tags=["health_check"])
app.include_router(samples.router, tags=["sample"])
app.include_router(items.router, tags=["item"], responses={404: {"description": "Not found"}})
app.include_router(tax.router, tags=["tax"])
app.include_router(todo.router, tags=["todo"])