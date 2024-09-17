import aiohttp


list_crypto = ['BTC', 'ETH', 'XMR', 'SOL', 'DOGE']

async def get_price_kucoin():
    url = 'https://api.kucoin.com/api/v1/prices'
    price = []
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            for i in range(len(list_crypto)):
                if response.status == 200:
                    data = await response.json()
                    bitcoin_price = data.get('data', {}).get(list_crypto[i])
                    if i == 0:
                        price.append(round(float(bitcoin_price), 5))
                    else:
                        price.append(round(price[0]/float(bitcoin_price), 5))
                else:
                    print(f'Ошибка при запросе: {response.status}')
                    return None
            return price
    
        




