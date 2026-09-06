# Inventory Management - Generic Types & PEP 695

A warehouse management system stores different types of items such as electronics, medicines, clothing, and grocery products. The developer wants a reusable repository that can work with any product type while maintaining type safety.

## Question

Design a generic repository using modern Python generic syntax.

1. Explain why generics are useful in this scenario.
2. Design a generic repository.
3. Use PEP 695-style generic type parameter syntax where appropriate.
4. Demonstrate the repository with two different product types.

## Generic Programming

Generic programming is a programming technique where we write one piece of code that can work with different data types.

## 1. Why Are Generics Useful in This Scenario?

### Example

A warehouse has:

* **Electronics** → Laptop, Mobile
* **Medicine** → Paracetamol, Syrup

We could create separate repositories:

* `ElectronicsRepository`
* `MedicineRepository`

This causes **code duplication**.

Instead, we can create one generic repository:

```text
Repository[T]
```

Here, `T` represents any product type.

```text
Repository[Electronics] → Laptop, Mobile
Repository[Medicine] → Paracetamol, Syrup
```

The same repository code can therefore be reused for different product types.

## Algorithm

1. Identify common repository operations.
2. Create one generic repository.
3. Use `T` as a type parameter.
4. Create `Repository[Electronics]`.
5. Create `Repository[Medicine]`.
6. Reuse the same code safely.

# Python Implementation

## Without Generics

```python
class ElectronicsRepository:

    def add(self, item):
        print("adding electronics:", item)


class MedicineRepository:

    def add(self, item):
        print("adding medicine:", item)


electronics = ElectronicsRepository()
medicine = MedicineRepository()

electronics.add("laptop")
medicine.add("paracetamol")
```

## Output

```text
Adding electronics: laptop
Adding medicine: paracetamol
```

# With Generics - One Class

```python
class Repository[T]:

    def add(self, item: T):
        print("adding:", item)


electronics = Repository[str]()
medicine = Repository[str]()

electronics.add("laptop")
medicine.add("paracetamol")
```

## Output

```text
adding: laptop
adding: paracetamol
```

# Time Complexity

```text
Time complexity without generics = O(1)

Time complexity with generics = O(1)
```
## 2. Design a Generic Repository
Based on the scenario using Generic programming

### Example:

Clothing:
101 → shirts
102 → Pants

Grocery:
201 → Books
202 → Shampoo

Instead of Creating 2 repositories

Create:

Repository[T]

T → Clothing, Grocery

## Algorithm:

1. Create a generic Repository[T].
2. Maintain an internal collection.
3. add(item):
       Add item to collection.

4. get_all():
       Return all items.

5. fine_by_id(id):
       Search for matching ID.

6. Return the result.



# Python implementation:
```python
class Repository[T]:

    def __init__(self):
        self.items: List[T] = []

    def add(self, item: T) → None:
        self.items.append(item)

    def get_all(self) → List[T]:
        return self.items

    def find_by_id(self, product_id: int) → T|None:
        for item in self.items:
            if item.id == product_id:
                return item
        return None

class Clothing:

    def __init__(self, id: int, name: str, size: str):
        self.id = id
        self.name = name
        self.size = size

    def __repr__(self):
        return f"{self.name} - size {self.size}"

class Grocery:

    def __init__(self, id: int, name: str, price: float):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"{self.name} - ₹{self.price}"
clothing_repo = Repository[Clothing]()
grocery_repo = Repository[Grocery]()

clothing_repo.add(
    Clothing(101, "T-shirt", "M")
)

grocery_repo.add(
    Grocery(201, "Book", 250)
)

print("Clothing:")
print(clothing_repo.get_all())

print("Grocery:")
print(grocery_repo.get_all())
```

## Output:

```text

Clothing:

[T-shirt - size M]

Grocery:

[Book - ₹50]
```

## Time Complexity:

```text

Best case: O(1)

Worst case: O(n)
```
# 3. PEP 695-Style Generic Type Parameter

Use PEP 695-style generic type parameter syntax where appropriate.

## Scenario

According to the scenario, use PEP 695-style generic type parameter syntax.

### Example

Imagine a warehouse repository containing:

```text
Repository[Electronics]
Repository[Medicine]
Repository[Clothing]
```

The same class can be reused.

## Algorithm

1. Create a `Repository[T]`.
2. `T` acts as a placeholder for a type.
3. Create `Repository[Electronics]`.
4. Create `Repository[Clothing]`.
5. Add objects to their appropriate repository.
6. Retrieve the objects.

## Python Implementation

```python
class Repository[T]:

    def __init__(self):
        self.items: list[T] = []

    def add(self, item: T):
        self.items.append(item)

    def get_all(self) -> list[T]:
        return self.items


class Electronics:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


class Clothing:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


electronics_repo = Repository[Electronics]()
clothing_repo = Repository[Clothing]()

electronics_repo.add(Electronics("Laptop"))
electronics_repo.add(Electronics("Mobile"))

clothing_repo.add(Clothing("T-shirt"))
clothing_repo.add(Clothing("Jeans"))

print("Electronics:")
print(electronics_repo.get_all())

print("Clothing:")
print(clothing_repo.get_all())
```

## Output

```text
Electronics:
[Laptop, Mobile]

Clothing:
[T-shirt, Jeans]
```

## Time Complexity

Best case: O(1)

Worst case: O(n)

# 4. Demonstrate the Repository with Two Different Product Types

According to the scenario using generic programming.

## Example

Our warehouse stores:

### Electronics:
```text
101 → Laptop
102 → Smartphone
````

### Clothing:

```text
201 → T-shirt
202 → Jeans
```

Created two repositories:

```text
Repository[Electronics]
Repository[Clothing]
```

## Algorithm

1. Define Electronics.
2. Define Clothing.
3. Create Generic Repository[T].
4. Create:

   ```text
   electronics_repo = Repository[Electronics]()
   clothing_repo = Repository[Clothing]()
   ```
5. Add respective products.
6. Retrieve products.

## Python Implementation

```python
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
```

## Output

```text
Electronics:
[Electronics(101, Laptop, ₹55000), Electronics(102, Smartphone, ₹25000)]

Clothing:
[Clothing(201, T-shirt, size=M), Clothing(202, Jeans, size=L)]

Search Electronics:
Electronics(101, Laptop, ₹55000)

Search Clothing:
Clothing(202, Jeans, size=L)
```

## Time Complexity

Best case: O(1)

Worst case: O(n)

