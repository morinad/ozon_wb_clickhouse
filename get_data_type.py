def get_data_type(value):
    if isinstance(value, str):
        # Список возможных форматов дат и времени
        date_formats = [
            '%Y-%m-%dT%H:%M:%S',  # ISO формат DateTime: 2024-09-01T21:20:10
            '%Y-%m-%d %H:%M:%S',  # DateTime с пробелом: 2024-09-01 21:20:10
            '%Y-%m-%d',  # Формат Date: 2021-09-08
            '%d-%m-%Y',  # Формат Date с днем в начале: 08-09-2021
            '%Y/%m/%d',  # Формат Date через слэш: 2024/09/01
            '%H:%M:%S'  # Формат Time: 21:20:10
        ]
        for date_format in date_formats:
            try:
                datetime.strptime(value, date_format)
                # Определяем тип на основе формата
                if date_format in ['%Y-%m-%d', '%d-%m-%Y', '%Y/%m/%d']:
                    return 'Date'  # Все эти форматы — это Date
                elif date_format == '%H:%M:%S':
                    return 'Time'  # Только время
                else:
                    return 'DateTime'  # Форматы с датой и временем
            except ValueError:
                continue  # Если строка не соответствует формату, проверяем дальше
        return 'String'  # Если это не дата и не время, возвращаем String

    elif isinstance(value, int):
        return 'UInt64'
    elif isinstance(value, float):
        return 'Float64'
    elif isinstance(value, bool):
        return 'UInt64'  # ClickHouse использует UInt64 для булевых значений
    else:
        return 'String'