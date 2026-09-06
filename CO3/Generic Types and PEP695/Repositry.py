class Repository[T]:

    def __init__(self):
        self.items: list[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def get_all(self) -> list[T]:
        return self.items

    def find_by_id(self, product_id: int) -> T | None:
        for item in self.items:
            if item.id == product_id:
                return item
        return None


class Electronics:

    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Electronics({self.id}, {self.name}, ₹{self.price})"


class Clothing:

    def __init__(self, id: int, name: str, size: str):
        self.id = id
        self.name = name
        self.size = size

    def __repr__(self):
        return f"Clothing({self.id}, {self.name}, size={self.size})"


electronics_repo = Repository[Electronics]()

electronics_repo.add(
    Electronics(101, "Laptop", 55000)
)

electronics_repo.add(
    Electronics(102, "Smartphone", 25000)
)


clothing_repo = Repository[Clothing]()

clothing_repo.add(
    Clothing(201, "T-shirt", "M")
)

clothing_repo.add(
    Clothing(202, "Jeans", "L")
)


print("Electronics:")
print(electronics_repo.get_all())

print("Clothing:")
print(clothing_repo.get_all())

print("Search Electronics:")
print(electronics_repo.find_by_id(101))

print("Search Clothing:")
print(clothing_repo.find_by_id(202))
