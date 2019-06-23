

i_code = ["22", "33", "44", "22"]
item = ["Apple", "Mango", "banana", "Apple"]
price = ["2", "3", "4", "2"]


class Product:
    id = str()
    items = str()
    prices = str()

    def __init__(self, id, items, prices):
        self.id = id
        self.items = items
        self.prices = prices


list_pros = list()
for i in range(1, 3):
    get = input("Enter value")
    get1 = input("Enter value item")
    get2 = input("Enter value price")
    pros = Product(get, get1, get2)
    list_pros.append(pros)

for get in list_pros:
    print(get.id, get.items, get.prices)
