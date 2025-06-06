class Menu:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        if not isinstance(item, Item):
            raise ValueError('item must be of type Item')
        self.items.append(item)
        print(f"Item {item.name} added to menu {self.name}")

class Item:
    def __init__(self, name):
        self.name = name

class MenuItem:
    all = []

    def __init__(self, menu, item, in_stock=True):
        self.menu = menu
        self.item = item
        self.in_stock = in_stock
        MenuItem.all.append(self)

    @property
    def menu(self):
        return self._menu
    
    @menu.setter
    def menu(self, value):
        if not isinstance (value, Menu):
            raise TypeError('value must be of type Menu')
        self._menu = value

    @property
    def item(self):
        return self._item
    
    @item.setter
    def item(self, value):
        if not isinstance(value, Item):
            raise TypeError('value must be of type Item')
        self._item = value

    def update_stock(self, value):
        if not isinstance(value, bool):
            raise ValueError('value must be of type bool')
        self.in_stock = value
        print(f"Updated item {self.item.name} for menu {self.menu.name} to be {'in stock' if value else 'out of stock'}")