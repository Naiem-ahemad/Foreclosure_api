from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

@app.get("/check")
def check():
    try:
        # Detect public IP location
        ip_info = requests.get("http://ip-api.com/json", timeout=5).json()
        country = ip_info.get("country", "Unknown")

        # Fetch the auction site HTML
        auction_url = "https://www.alachua.realforeclose.com"
        response = requests.get(auction_url, timeout=10)
        html_content = response.text

        return JSONResponse({
            "status": "success",
            "country": country,
            "auction_site_html": html_content[:500]  # First 500 chars for brevity
        })

    except Exception as e:
        return JSONResponse({
            "status": "error",
            "message": str(e)
        })
