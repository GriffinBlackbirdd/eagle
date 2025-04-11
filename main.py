from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Create templates directory if it doesn't exist
templates_dir = "templates"
os.makedirs(templates_dir, exist_ok=True)

# Mount static files directory
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory=templates_dir)

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/resume", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("resume.html", {"request": request})

@app.get("/projects", response_class=HTMLResponse)
async def read_projects(request: Request):
    return templates.TemplateResponse("project.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)