from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from monorepo.healthai.src.api.ledgers.router import healthai_router

app = FastAPI()

app.include_router(healthai_router, prefix="/healthai", tags=["HealthAI"])


@app.get("/", tags=["Default"], include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")
