from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.app.api.routes.summarize import router as summarize_router
from backend.app.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(summarize_router)