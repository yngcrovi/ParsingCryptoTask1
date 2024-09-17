from send_email.send_email import send_message_email

async def price_crypto(title_crypto: list[str], get_price, service, market_name: str):
    price = await get_price()
    actual_data = await service.select_crypto()
    if not actual_data:
        data = []
        for i in range(len(price)):
            body = {
                'title': title_crypto[i],
                'min_price': price[i],
                'max_price': price[i],
                'difference': 0,
                'total_amount': round(3 * price[i], 5)
            }
            data.append(body)
        await service.insert_crypto(data)
        return 
    arr_actual_crypto = []
    for i in range(len(actual_data)):
        help_dict: dict = actual_data[i].model_dump()
        arr_actual_crypto.append(help_dict)
    update_value = []
    email_data = []
    update_arr_title = []
    for i in range(len(price)):
        if arr_actual_crypto[i]['max_price'] < price[i]:
            help_dict = {}
            update_arr_title.append(title_crypto[i])
            help_dict['max_price'] = price[i]
            help_dict['difference'] = round(((
                help_dict['max_price'] - arr_actual_crypto[i]['max_price']
                )/(arr_actual_crypto[i]['max_price'])) * 100, 8)
            help_dict['total_amount'] = 3 * help_dict['max_price']
            update_value.append(help_dict)
            if help_dict['difference'] >= 0.001:
                help_dict['title'] = title_crypto[i]
                email_data.append(help_dict)
        if arr_actual_crypto[i]['min_price'] > price[i]:
            help_dict = {}
            update_arr_title.append(title_crypto[i])
            help_dict['min_price'] = price[i]
            update_value.append(help_dict)
    if update_value:
        await service.update_crypto(update_arr_title, update_value)
        if email_data:
            str_email = ''
            for i in range(len(email_data)):
                str_email += email_data[i]['title'] + ' - ' + ' повышена на: ' + str(email_data[i]['difference'])
                if i+1 != len(email_data):
                    str_email += ', '
                else:
                    str_email += '.'
            body = f"На сайте {market_name}: {str_email}"
            return body