def remove_outliers(data, min_val, max_val):
    i = 0
    while i < len(data):
        if data[i] < min_val or data[i] > max_val: data.pop(i)
        else: i += 1
    return data
a = list(map(int, input().split()))
min_val, max_val= map(int, input().split())
print(f"Original measurements: {a}")
print(f"Cleaned measurements:  {remove_outliers(a, min_val, max_val)}")
print("--------------------")