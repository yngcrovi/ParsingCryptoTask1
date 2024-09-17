from fastapi import FastAPI
import asyncio
from track_crypto.track_binance import price_binance
from track_crypto.track_kucoin import price_kucoin
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from endpoint.binance_method import route as binance
from endpoint.kucoin_method import route as kucoin
from send_email.send_email import send_message_email

app = FastAPI()
scheduler = AsyncIOScheduler()

app.include_router(binance)
app.include_router(kucoin)


async def request_actual_crypto():
    while True:
        massage = ''
        massage_binance = await price_binance()  
        massage_kucoin = await price_kucoin()
        print(massage_binance, massage_kucoin)
        if massage_binance:
            massage += massage_binance + '\n'
        if massage_kucoin: 
            massage += massage_kucoin + '\n'
        if massage:
            send_message_email(massage)
        await asyncio.sleep(10)

@app.on_event("startup")
async def start_periodic_task():
    scheduler.add_job(request_actual_crypto)  
    scheduler.start()

@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()






