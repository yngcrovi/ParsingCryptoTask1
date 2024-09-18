from pars_crypto.kucoin_actions import get_price_kucoin
from repositoy.service.kucoin_service import kucoin_service
from .track_crypto import price_crypto

title_crypto = ['BTC/USDT', 'BTC/ETH', 'BTC/XMR', 'BTC/SOL', 'BTC/DOGE']

async def price_kucoin():
    massage = await price_crypto(title_crypto, get_price_kucoin, kucoin_service, 'Kucoin')
    return massage
