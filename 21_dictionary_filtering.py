# Question: Filter the dictionary by removing all items with a value of
# greater than 1.

d = {"a": 1, "b": 2, "c": 3}

# Expected output:
# {'a': 1}

# e = {}
# for k, v in d.items():
#     if v <= 1:
#         e[k] = v

# print(e)

d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)
