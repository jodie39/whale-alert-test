from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Whale Alert API is running"}

async def check_wallets():
    while True:
        print("🐋 Checking whale wallets...")
        await asyncio.sleep(30)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(check_wallets())
