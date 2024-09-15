def analyze_column_types(data):
    # Определяем тип для каждого столбца
    column_types = {}
    # Проходим по всем строкам в данных
    for row in data:
        for column, value in row.items():
            value_type = get_data_type(value)  # Определяем тип данных
            if column not in column_types:
                column_types[column] = set()  # Создаем множество для уникальных типов
            column_types[column].add(value_type)
    # Приводим типы столбцов к общему типу
    final_column_types = {}
    for column, types in column_types.items():
        if len(types) == 1:
            final_column_types[column] = next(iter(types))  # Если тип один, оставляем его
        elif 'Float64' in types or ('UInt64' in types and 'Float64' in types):
            final_column_types[column] = 'Float64'  # Если встречаются int и float, выбираем float
        else:
            final_column_types[column] = 'String'  # Если разные типы, делаем строкой
    create_table_query = []
    for field, data_type in final_column_types.items():
        create_table_query.append(f"{field} {data_type}")
    return create_table_query