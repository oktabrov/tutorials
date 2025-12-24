import itertools
import random
lst = ['Tigers', 'Dragons', 'Eagles', 'Sharks', 'Wolves', 'Bears']
random.shuffle(lst)
a = list(itertools.combinations(lst, 2))
k = 1
print('--- Tournament Schedule ---')
for i, j in a:
    print(f"Match {k}: {i} vs {j}")
    k += 1
print("---------------------------")
print(f"Total Matches to play: {len(a)}")