import csv
from product import Product

FILENAME = "products.csv"
PRODUCT_FIELDNAMES = ("id", "name", "price")

def product_has_id(id, product_list):
    for product in product_list:
        if product.id == id:
            return True
    return False

def enlist_product(id, name, price, product_list):
    if product_has_id(id, product_list):
        print(f"There is already a product for sale with id: {id}")
        return
    product = Product(id, name, price)
    product_list.append(product)
    write_products_to_file(FILENAME, product_list)
    print(f"Product with id: {id} was enlisted")

def remove_product(id, product_list):
    for i in range(len(product_list)):
        if product_list[i].id == id:
            return product_list.pop(i)
    return None

def sell_product(id, product_list):
    if product_has_id(id, product_list):
        product = remove_product(id, product_list)
        write_products_to_file(FILENAME, product_list)
        print(f"{product.name} has been sold")
    else:
        print(f"Product with id {id} was not found")

def print_all_products(product_list):
    for product in product_list:
        print(product)

def write_products_to_file(filename, product_list):
    with open(filename, "w", newline="") as file_object:
        writer = csv.DictWriter(file_object, PRODUCT_FIELDNAMES)
        writer.writeheader()
        for product in product_list:
            writer.writerow(product.to_dict())

def parse_command(command, product_list):
    if command == "":
        return

    command_list = command.split()

    if command_list[0] == "enlist":
        if len(command_list) < 4:
            print("Invalid command")
            return
        id = command_list[1]
        name = command_list[2]
        price = command_list[3]
        enlist_product(id, name, price, product_list)

    elif command_list[0] == "sell":
        if len(command_list) < 2:
            print("Invalid command")
            return
        id = command_list[1]
        sell_product(id, product_list)

    elif command_list[0] == "print":
        print_all_products(product_list)

def read_products_from_file(filename):
    product_list = []
    try:
        with open(filename, newline="") as file_object:
            reader = csv.DictReader(file_object)
            for row in reader:
                product_list.append(
                    Product(
                        row["id"],
                        row["name"],
                        row["price"]
                    )
                )
    except FileNotFoundError:
        pass
    return product_list

def main():
    product_list = read_products_from_file(FILENAME)
    command = ""
    while command != "quit":
        command = input("Enter a command: ").lower().strip()
        parse_command(command, product_list)

main()