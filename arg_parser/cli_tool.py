import argparse
from models import User

users = {}

def add_user(args):
    user = users.get(args.name) or User(args.name)
    print(f"Added user {user.name}")


def add(args):
    first_number = float(args.number_1)
    second_number = float(args.number_2)
    print(f"These add together as {first_number + second_number}")

def subtract(args):
    first_number = float(args.number_1)
    second_number = float(args.number_2)
    print(f"These add together as {first_number - second_number}")

def main():
    parser = argparse.ArgumentParser(description="Customer parser")
    subparsers = parser.add_subparsers()

    add_parser = subparsers.add_parser("add", help="Enter two numbers to add")
    add_parser.add_argument("number_1", help="Enter your first number")
    add_parser.add_argument("number_2", help="Enter your second number")
    add_parser.set_defaults(func=add)

    subtract_parser = subparsers.add_parser("subtract", help="Enter two numbers to subtract")
    subtract_parser.add_argument("number_1", help="Enter your first number")
    subtract_parser.add_argument("number_2", help="Enter your second number")
    subtract_parser.set_defaults(func=subtract)

    args = parser.parse_args()
    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()