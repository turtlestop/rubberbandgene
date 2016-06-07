import sys
from collections import defaultdict

def rubberband(gene, strn):
    n = int(strn)
    genecounts = defaultdict(lambda: 0)
    for l in gene:
        genecounts[l] += 1
    target = int(int(n) / 4)
    surplus_counts = {key: value - target
                      for key, value in genecounts.items()
                      if value > target}

    left = 0
    right = sum(surplus_counts.values())
    if right == 0:
        return 0
    best = n
    substring_counts = defaultdict(lambda: 0)
    for l in gene[left:right]:
        substring_counts[l] += 1

    while left < n:
        satisfied = all([substring_counts[k]>=surplus_counts[k]
               for k in surplus_counts])
        if satisfied:
            best = min(best, right-left)
            substring_counts[gene[left]] -=1
            left += 1
        else:
            if right<n:
                substring_counts[gene[right]] +=1
                right += 1
            else:
                return best
    return best

imp = sys.stdin.read().split('\n')
print(rubberband(imp[1], imp[0]))
