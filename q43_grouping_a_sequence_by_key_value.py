a=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
result = {}
for k, v in a:
    # print(v)
        result.setdefault(k, []).append(v)
print(result)
