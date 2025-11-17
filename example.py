from toon import encode, decode

data = {"name": "Alice", "age": 30}
# print(encode(data))

users = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35},
]
# print(encode(users))


data = {
    "metadata": {"version": 1, "author": "test"},
    "items": [
        {"id": 1, "name": "Item1"},
        {"id": 2, "name": "Item2"},
    ],
    "tags": ["alpha", "beta", "gamma"],
}

toon_encode_str = encode(data)
print(toon_encode_str)

decode_json = decode(toon_encode_str)
print(decode_json)


text = """
records[5,] {
  { date: "2024-01-15", name: "Alice", salary: 95000 }
  { date: "2024-02-20", name: "Bob", salary: 87000 }
  { date: "2024-02-21", name: "Rana", salary: 88000 }
  { date: "2024-02-22", name: "Kabir", salary: 87000 }
  { date: "2024-02-23", name: "Kamal", salary: 87000 }
}
"""

print(decode(text))