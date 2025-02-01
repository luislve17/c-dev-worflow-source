from fastapi import FastAPI
from api.numbers.endpoints import router as numbers_router

app = FastAPI()

app.include_router(numbers_router)
