def find_longest_run(data):
    if len(data) == 0: return 0
    item = data[0]
    i = 0; s = 1; m = 1
    while i + 1 < len(data):
        if item == data[i+1]:
            s += 1
            # print(s, m, item, data[i+1])
            if s > m: m = s
        else:
            item = data[i + 1]
            s = 1
        i += 1
    return m
a = list(input().split())
print(f"Longest run in {a}: {find_longest_run(a)}")
