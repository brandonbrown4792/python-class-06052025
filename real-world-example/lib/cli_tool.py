import argparse
from models import Item, Menu, MenuItem

menus = {}
items = {}

def add_item(args):
    item = items.get(args.item) or Item(args.item)
    print(f"Created item {item.name}")

def add_menu(args):
    menu = menus.get(args.menu) or Menu(args.menu)
    print(f"Created menu {menu.name}")

def add_item_to_menu(args):
    menu = menus.get(args.menu) or Menu(args.menu)
    item = items.get(args.item) or Item(args.item)
    menu.add_item(item)

def update_menu_item_stock(args):
    menu = menus.get(args.menu) or Menu(args.menu)
    item = items.get(args.item) or Item(args.item)
    menu_item = next((menu_item for menu_item in MenuItem.all if menu_item.menu == menu and menu_item == item), MenuItem(menu, item))

    in_stock = False
    if args.in_stock.lower() in ['yes', 'true', 'in stock']:
        in_stock = True
    menu_item.update_stock(in_stock)

parser = argparse.ArgumentParser(description="Menu item argument parser")
subparsers = parser.add_subparsers()

add_item_subparser = subparsers.add_parser("add-item", help="Add an item")
add_item_subparser.add_argument("item", help="Name of the item")
add_item_subparser.set_defaults(func=add_item)

add_menu_subparser = subparsers.add_parser("add-menu", help="Add a menu")
add_menu_subparser.add_argument("menu", help="Name of the menu")
add_menu_subparser.set_defaults(func=add_menu)

add_menu_item_subparser = subparsers.add_parser("add-item-to-menu", help="Add item to menu")
add_menu_item_subparser.add_argument("menu", help="Name of the menu")
add_menu_item_subparser.add_argument("item", help="Name of the item")
add_menu_item_subparser.set_defaults(func=add_item_to_menu)

update_menu_item_stock_parser = subparsers.add_parser("update-menu-item-stock", help="Update stock of item")
update_menu_item_stock_parser.add_argument("menu", help="Name of the menu")
update_menu_item_stock_parser.add_argument("item", help="Name of the item")
update_menu_item_stock_parser.add_argument("in_stock", help="In stock - either True or False")
update_menu_item_stock_parser.set_defaults(func=update_menu_item_stock)

args = parser.parse_args()
if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()
