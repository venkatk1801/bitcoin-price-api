# 📈 Real-Time Bitcoin Price Tracker API (FastAPI + Chart.js)

This project is a FastAPI application that fetches real-time Bitcoin prices from the internet using the CoinGecko public API and displays them in:

- A **REST API endpoint** (`/bitcoin-price`)
- A **live chart view** (at `/`) using **Chart.js**
- Supports prices in **USD** and **INR**

---

## 🚀 Features

- 🔄 Fetch real-time Bitcoin price (via `/update-price`)
- 📊 View historical price graph (via `/`)
- 🌐 Uses CoinGecko’s free and open API
- 🎨 Visualizes Bitcoin price trends using HTML + Chart.js
- 🧠 Built with FastAPI and can be deployed on platforms like Render or Railway

---

## 📦 Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Requests
- Jinja2

Install dependencies:
```bash
pip install -r requirements.txt
