def get_orders(api_key, date):
    date_rfc3339 = f"{date}T00:00:00.000Z"
    url = "https://statistics-api.wildberries.ru/api/v1/supplier/orders"
    headers = {
        "Authorization": api_key,
    }
    params = {
        "dateFrom": date_rfc3339,
        "flag": 1,  # Для получения всех заказов на указанную дату
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()