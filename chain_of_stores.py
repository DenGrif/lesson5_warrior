class Store:
    def __init__(self, name, address):
        # Конструктор, который инициализирует название, адрес и пустой ассортимент товаров.
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        # добавление товара в ассортимент.
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен в магазин {self.name} по цене {price}")

    def remove_item(self, item_name):
        # удаление товара из ассортимента.
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удалён из магазина.{self.name}")
        else:
            print(f"Товар '{item_name}' не найден в магазине '{self.name}'")

    def get_price(self, item_name):
        # получение цены товара по его названию.
        # Возвращает None, если товар не найден.
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        # Обновление цены
        if item_name in self.items:
            print(f"Цена '{item_name}' на товар обновлена до '{new_price}'.")
        else:
            print(f"Товар '{item_name}' не найден в магазине '{self.items}'.")

    def __repr__(self):
        # текстовое представления магазина.
        return f"Магазин: {self.name}, Адрес: {self.address}, Товары: {self.items}"

# Создаём магазины

store1 = Store("Магазин у дома", "ул. Ленина, 12")
store2 = Store("Фруктовый сад", "ул. Садовая, 8")
store3 = Store("Всё для дома", "ул. Строителей")

# Добавляем товары в магазины
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)

store2.add_item("oranges", 1.0)
store2.add_item("grapes", 2.5)

store3.add_item("detergent", 3.0)
store3.add_item("sponge", 1.2)

# Тестирование методов для одного из магазинов
print("\n--- Тестирование методов для 'Магазин у дома' ---")
print(store1)

# Добавляем новоый товар
store1.add_item("bread", 0.8)

# Обновляем цены товара
store1.update_price("bananas", 0.65)

# Получение цены товара
price = store1.get_price("apples")
print(f"Цена на apples: {price}")

# Удаление товара
store1.remove_item("apples")

# Проверка отсутствующего товара
price = store1.get_price("apples")
if price is None:
    print("Товар apples отсутствует в магазине.")

