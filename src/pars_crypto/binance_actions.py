import aiohttp

DOMAIN_BINANCE_GET_CRYPTO = 'https://api.binance.com/api/v3/ticker/price?symbol='
BTC_URL = DOMAIN_BINANCE_GET_CRYPTO + 'BTCUSDT'
ETH_URL = DOMAIN_BINANCE_GET_CRYPTO + 'ETHBTC'
XMR_URL = DOMAIN_BINANCE_GET_CRYPTO + 'XMRBTC'
SOL_URL = DOMAIN_BINANCE_GET_CRYPTO + 'SOLBTC'
RUB_URL = DOMAIN_BINANCE_GET_CRYPTO + 'BTCRUB'
DOGE_URL = DOMAIN_BINANCE_GET_CRYPTO + 'DOGEBTC'
url_crypto = [BTC_URL, ETH_URL, XMR_URL, SOL_URL, RUB_URL, DOGE_URL]

async def get_price_binance():
    async with aiohttp.ClientSession() as session:
        price = []
        for url in url_crypto:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()  
                    if float(data['price']) < 1:
                        price.append(round(1/float(data['price']), 5))
                    else:
                        price.append(round(float(data['price']), 5))
        return price
            
    