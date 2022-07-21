# Question: Calculate the sum of all dictionary values.

d = {"a": 1, "b": 2, "c": 3}

# Expected output:
#  6


def add_function(x):
    sum = 0
    for v in x.values():
        sum += v
    return sum


print(add_function(d))
