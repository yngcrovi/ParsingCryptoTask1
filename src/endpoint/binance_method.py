from fastapi import APIRouter
from repositoy.service.binance_service import binance_service

route = APIRouter(
    tags=['Binance'],
    prefix='/binance'
)

@route.get("/get")
async def get_crypto():
    actual_data = await binance_service.select_crypto()
    arr_actual_crypto = []
    for i in range(len(actual_data)):
        help_dict: dict = actual_data[i].model_dump()
        arr_actual_crypto.append(help_dict)
    return arr_actual_crypto