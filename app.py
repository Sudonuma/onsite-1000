from typing import List, Optional, Tuple
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


# Create the FastAPI instance
app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Device

@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    """
    Handles the GET request for the index page.

    Args:
        - request (Request): The request object.

    Returns:
        - TemplateResponse: HTML response.
    """
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)


@app.get("/EDA", response_class=HTMLResponse)
async def EDA(request: Request):
    """
    Handles the GET request for the EDA page.

    Args:
        - request (Request): The request object.

    Returns:
        - TemplateResponse: HTML response.
    """
    context = {"request": request}
    return templates.TemplateResponse("EDA.html", context)

