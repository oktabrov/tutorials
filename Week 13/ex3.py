import random as r
import statistics as s
results = []
for i in range(1_000):
    s1 = r.randrange(1, 7)
    s2 = r.randrange(1, 7)
    results.append(s1+s2)
print("--- Simulation Results (1000 rolls) ---")
print(f"Mean: {s.mean(results)}")
print(f"Median: {s.median(results)}")
print(f"Mode: {s.mode(results)}")