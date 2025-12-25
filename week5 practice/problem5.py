def calculate_moving_average(data, window_size):
    a = []
    for i in range(len(data) - window_size + 1):
        # print(data[i: i + window_size])
        a.append(round(sum(data[i: i + window_size])/window_size, 1))
    return a
data = list(map(int, input().split()))
window_size = int(input())
output = calculate_moving_average(data, window_size)
print(f"Moving average (window {window_size}{" - too big" if len(output) == 0 else ''}) of {data}: {output}")