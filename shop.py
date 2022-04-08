class Product:
    __id = 1
    def __init__(self, title, desc, price):
        self.id = Product.__id
        self.title = title
        self.desc = desc
        self.price = price
        Product.__id += 1


class Order:
    def error(self, user):
        if user.bill < user.cart.get('total_price'):
            print(f'Извините, {user.name} у вас не достаточно средств')
            print(f'Пополните баланс, или уберите что-то из корзины')
            if input('Пополнить баланс? (y): ') == 'y':
                amount = int(input('Введите сумму: '))
                user.add_bill(amount)
            

    def __init__(self, user):
        while user.bill < user.cart.get('total_price'):
            self.error(user)
        user.bill -= user.cart.get('total_price')
        print(f'Ваш заказ едет по адресу {user.address}')
        user.show_cart()
        user.clear_cart()
        print(f'У вас осталось {user.bill} денег')

class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.bill = 0
        self.cart = {'total_price':0}

    def add_bill(self, amount):
        self.bill += amount

    def add_to_card(self, *products):
        for product in products:
            self.cart[product.id] = {
                                    'title':product.title,
                                    'price':product.price
                                    }
            self.cart['total_price'] += product.price 

    def remove_from_cart(self, *products):
        for product in products:
            try:
                self.cart.pop(product.id)
                self.cart['total_price'] -= product.price
            except:
                print(f'{product.title} в вашей карзине нет')

    def show_cart(self):
        from pprint import pprint
        print(f'=============\n{self.name}')
        pprint(self.cart)
        print(f'=============')

    def clear_cart(self):
        self.cart.clear()
        self.cart['total_price'] = 0

ice_cream1 = Product('Магнат', 'Очень вкусное мороженное', 96)
ice_cream2 = Product('Смак', 'С кунжутом, тоже вкусно', 15)
plov = Product('Плов', 'Узгенский плов с бараниной', 150)
salatic = Product('Шакарап', 'Помидорки', 50)

nurkamila = User('Нуркамила', 'Аламедин 1')
nurkamila.add_bill(1000)
nurkamila.add_to_card(ice_cream1, salatic, plov)
# nurkamila.show_cart()


uluk = User('Улук', 'Тунгуч')
uluk.add_bill(150)
uluk.add_to_card(ice_cream2, plov)
# uluk.show_cart()

nurkamila.remove_from_cart(plov)
# nurkamila.show_cart()

uluk_order = Order(uluk)
print(uluk.bill)