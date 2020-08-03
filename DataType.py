complex_one = 1j
print(type(complex_one), complex_one)

list_one = ["apple", "orange", "cherry"]
print(type(list_one), list_one)

tuple_one = ("apple", "orange", "cherry")
print(type(tuple_one), tuple_one)

range_one = range(6)
print(type(range_one), range_one)

# basically a map
dict_one = {"name": "John", "age": 36}
print(type(dict_one), dict_one)
print(dict_one.get("name"))

set_one = {"one", "two", "three"}
print(type(set_one), set_one)

f_set = frozenset(set_one)
print(type(f_set), f_set)

byte_one = b"Hello"
print(type(byte_one), byte_one)

byte_array_one = bytearray(5)
print(type(byte_array_one), byte_array_one)

memview_one = memoryview(bytes(5))
print(type(memview_one), memview_one)
