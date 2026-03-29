import random
# Constant settings
RADIUS = 1
TOTAL = 1000000
SQ_AREA = (RADIUS * 2) * (RADIUS * 2)
CIRCLED = 0

# Randomly generate points and count those inside the circle
for _ in range(TOTAL):
    x = random.uniform(-RADIUS, RADIUS)
    y = random.uniform(-RADIUS, RADIUS)
    if x * x + y * y <= RADIUS * RADIUS:
        CIRCLED += 1

# Estimate pi based on the number of points inside the circle
pi = (CIRCLED / TOTAL) * SQ_AREA
print(f"Estimated value of pi is: {pi}")
