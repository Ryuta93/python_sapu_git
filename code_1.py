#問題3-1
class Item:
    def __init__(self, id, name, price, purchase_price):
        self.id = id
        self.name = name
        self.price = price
        self.purchase_price = purchase_price
        
    def cost_rate(self):
        rate = self.purchase_price / self.price
        return rate

item_1 = Item('A0001', '半袖クールTシャツ', 5000, 2250)
item_1.price
rate = item_1.cost_rate()
print(rate)