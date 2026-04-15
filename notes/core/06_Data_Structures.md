# 06: Python Data Structures

Data structures are a way of organizing and storing data so that they can be accessed and worked with efficiently.

## Lists
- **Ordered:** The items have a defined order, and that order will not change.
- **Mutable:** You can change, add, and remove items in a list after it has been created.
- **Allow Duplicates:** Lists can have items with the same value.
- Created with square brackets `[]`.

**Example:**
```python
my_list = ["apple", "banana", "cherry"]
print(my_list[1]) # Access item: "banana"

my_list.append("orange") # Add item
my_list[0] = "blackcurrant" # Change item
my_list.remove("banana") # Remove item
print(my_list)
```

## Tuples
- **Ordered:** Same as lists.
- **Immutable:** You cannot change, add, or remove items after the tuple has been created.
- **Allow Duplicates:** Same as lists.
- Created with round brackets `()`.

**Example:**
```python
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0]) # Access item: "apple"

# The following would cause an error:
# my_tuple[0] = "kiwi"
# my_tuple.append("orange")
```
**Why use tuples?** They are faster than lists. Use them for data that you know should not be changed.

## Sets
- **Unordered:** The items in a set do not have a defined order.
- **Mutable:** You can add or remove items from a set.
- **No Duplicates:** Sets cannot have two items with the same value.
- Created with curly brackets `{}` or the `set()` constructor.

**Example:**
```python
my_set = {"apple", "banana", "cherry"}
my_set.add("orange") # Add item
my_set.remove("banana") # Remove item
print(my_set)

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) # {1, 2, 3, 4, 5}
print(set1.intersection(set2)) # {3}
```

## Dictionaries
- **Ordered (as of Python 3.7):** Items have a defined order.
- **Mutable:** You can change, add, or remove items.
- **No Duplicate Keys:** Keys must be unique.
- Store data in `key:value` pairs.
- Created with curly brackets `{}`.

**Example:**
```python
my_dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(my_dict["model"]) # Access value: "Mustang"

my_dict["year"] = 2020 # Change value
my_dict["color"] = "red" # Add new key-value pair
my_dict.pop("model") # Remove item

print(my_dict.keys()) # Get all keys
print(my_dict.values()) # Get all values
print(my_dict.items()) # Get all key-value pairs
```
