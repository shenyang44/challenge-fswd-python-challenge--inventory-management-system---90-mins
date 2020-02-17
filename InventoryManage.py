class Store():
    ware_list = []

    def __init__(self, name):
        self.name = name

    def new_ware(self, ware_house):
        self.ware_list.append(ware_house)

    def store_search(self, product_name):
        for ware in self.ware_list:
            for product in ware.products:
                if product == product_name:
                    print(
                        f'Yeah we selling some {product.name} for RM{product.price} \n at: {ware.address}')


class Warehouse():
    def __init__(self, address):
        self.address = address
        self.products = []

    def add(self, name, addition=0):
        if self.products.count(name):
            index = self.products.index(name)
            self.products[index].quantity += addition
        else:
            self.products.append(name)

    def remove(self, product, reduction):
        index = self.products.index(product)
        self.products[index].quantity -= reduction

    def __str__(self):
        print_ware_stock = ''
        for each in self.products:
            print_ware_stock += f'\n{each} \n'

        return print_ware_stock


class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, RM {str(self.price)}, quantity: {self.quantity}'


chair = Product('chairem', 200, 10)
ware1 = Warehouse('road 1')
main_store = Store('store_name')
table = Product('table-san', 500, 5)
main_store.new_ware(ware1)
ware1.add(chair)
ware1.add(table)
ware1.remove(chair, 5)

main_store.store_search(chair)
print(ware1)
