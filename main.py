from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from routers import image, caption
from services import startup

app = FastAPI(
    title="Lauzhack 2023",
    description="AXA's challenge CogVLM API",
    docs_url="/docs",
    redoc_url="/redoc",
    version="0.1.0",
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
)

app.include_router(image.router)
app.include_router(caption.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

startup.load_cog()


@app.get("/")
def root():
    return RedirectResponse(url="/docs")
