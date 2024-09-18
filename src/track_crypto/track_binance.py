from pars_crypto.binance_actions import get_price_binance
from repositoy.service.binance_service import binance_service
from .track_crypto import price_crypto

title_crypto = ['BTC/USDT', 'BTC/ETH', 'BTC/XMR', 'BTC/SOL', 'BTC/RUB', 'BTC/DOGE']

async def price_binance():
    massage = await price_crypto(title_crypto, get_price_binance, binance_service, 'Binance')
    return massage
