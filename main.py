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
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
            "Sec-CH-UA": '"Chromium";v="140", "Not=A?Brand";v="24", "Google Chrome";v="140"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Platform": '"Windows"',
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
            "Cookie": "cfid=bc2e9d5e-50a5-4dd0-9de2-189bfcf818b2; cftoken=0; CF_CLIENT_ALACHUA_REALFORECLOSE_TC=1757780602519; AWSALB=FuEML0sLB1IBAxjj9/ifBhR5s/K2CLOAYJzzI690I/RT09zOk18nOXWueKikbgraUolej/vfm8WuPrCCD5PuJNmmmrr4441g1sSlMRaDQt22AA3TzxPY1MQ6piw5; AWSALBCORS=FuEML0sLB1IBAxjj9/ifBhR5s/K2CLOAYJzzI690I/RT09zOk18nOXWueKikbgraUolej/vfm8WuPrCCD5PuJNmmmrr4441g1sSlMRaDQt22AA3TzxPY1MQ6piw5; CF_CLIENT_ALACHUA_REALFORECLOSE_LV=1757780971246; CF_CLIENT_ALACHUA_REALFORECLOSE_HC=9"
        }

        response = requests.get(auction_url, headers=headers, timeout=10)
        html_content = response.text

        return JSONResponse({
            "status": "success",
            "country": country,
            "auction_site_html": html_content[:500]  # First 500 chars
        })

    except Exception as e:
        return JSONResponse({
            "status": "error",
            "message": str(e)
        })
