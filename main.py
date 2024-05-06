from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime  # Import datetime module

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time
    return templates.TemplateResponse("index.html", {"request": request, "current_time": current_time})

@app.get("/whats-the-time", response_class=HTMLResponse)
async def read_whats_the_time(request: Request):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current time
    return templates.TemplateResponse("index.html", {"request": request, "current_time": current_time})
