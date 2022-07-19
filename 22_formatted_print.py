# Create a dictionary of keys a, b, c, where each key has a value
# from list 1 to 10, 11 to 20, and 21 to 30 respectively and print out

d = {"a": list(range(1, 11)), "b": list(
    range(11, 21)), "c": list(range(21, 31))}


print(
    f"Key 'a' is {d['a']}\n"
    f"Key 'b' is {d['b']}\n"
    f"Key 'c' is {d['c']}\n"
)
