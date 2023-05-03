from fastapi import FastAPI
from api import health_check, samples, items, tax

app = FastAPI()

app.include_router(health_check.router)
app.include_router(samples.router)
app.include_router(items.router)
app.include_router(tax.router)