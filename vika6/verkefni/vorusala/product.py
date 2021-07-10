class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }

    def __str__(self):
        return f"ID: {self.id}    Name: {self.name}    Price:{self.price}kr"