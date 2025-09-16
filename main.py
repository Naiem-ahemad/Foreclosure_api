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

        auction_url = "https://www.alachua.realforeclose.com"
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
        }

        response = requests.get(auction_url, headers=headers, timeout=10)
        html_content = response.text

        return JSONResponse({
            "status": "success",
            "country": country,
            "auction_site_html": html_content # First 500 chars
        })

    except Exception as e:
        return JSONResponse({
            "status": "error",
            "message": str(e)
        })
