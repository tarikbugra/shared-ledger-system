from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from monorepo.core.config import settings
from monorepo.healthai.src.api.ledgers.router import healthai_router
from monorepo.travelai.src.api.ledgers.router import travelai_router


def create_app():
    """Initialize FastAPI app."""
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.DESCRIPTION,
        version=settings.VERSION,
        contact={
            "name": settings.CONTACT_NAME,
            "email": settings.CONTACT_MAIL,
        },
        redoc_url=None,
        docs_url="/docs",
    )
    app.include_router(healthai_router, prefix="/healthai", tags=["HealthAI"])
    app.include_router(travelai_router, prefix="/travelai", tags=["TravelAI"])
    return app


app = create_app()


@app.get("/", tags=["Default"], include_in_schema=False)
async def root():
    return RedirectResponse(url="/docs")
