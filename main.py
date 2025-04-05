from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import requests
from datetime import datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")
COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

# Store prices in memory (for demo)
price_history = []

@app.get("/", response_class=HTMLResponse)
async def show_chart(request: Request):
    return templates.TemplateResponse("chart.html", {"request": request, "prices": price_history})

@app.get("/update-price")
def update_price():
    params = {"ids": "bitcoin", "vs_currencies": "usd,inr"}
    response = requests.get(COINGECKO_URL, params=params)
    if response.status_code != 200:
        return {"error": "Failed to fetch"}
    data = response.json()
    timestamp = datetime.now().strftime("%H:%M:%S")

    entry = {
        "time": timestamp,
        "usd": data["bitcoin"]["usd"],
        "inr": data["bitcoin"]["inr"]
    }
    price_history.append(entry)
    return entry
