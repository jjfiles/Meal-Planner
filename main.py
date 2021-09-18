from ingredients import combined
import random

# serving sizes
# Protein 6oz-8oz
# Veggies 1- 1.5 cups 
# Fruit 1-1.5 cups

# Lunch:
# 1 protein, 1 vegetable, 1 carb
l = [1, 1, 1]

# Dinner:
# 1 protein, 2 vegetables
d = [1, 2, 0]

#pick ingredients
def pick(m):
    out = []
    for i in range(3):
        for ingr in range(m[i]):
            tmp = random.choice(combined[ingr])
            if tmp not in out:
                out.append(tmp)
    return out

print(pick(d))
print(pick(l))

# search meals

# compare to last week

# re-adjust if necessary