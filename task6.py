def run_task6():
    result = []
    while 1 == 1:
        prod_num = (input("Введите номер товара: "))
        prod_name = (input("Введите название товара: "))
        prod_price = (input("Введите цену товара: "))
        prod_count = (input("Введите количество товара: "))
        result.append((prod_num, {'название': prod_name, 'цена': prod_price, 'количество': prod_count}))
        quest = input("Хотите ещё? (Д/Н): ")
        if quest.upper() == "Н":
            break
    print(f'Товары - {result}')

    analytics = {}
    for num, properties in result:
        for prop_key, prop_value in properties.items():
            if analytics.get(prop_key):
                analytics[prop_key].append(prop_value)
            else:
                analytics[prop_key] = [prop_value]
    print(f'Аналитика - {analytics}')
