import random

# Constant settings
RADIUS = 1
NUM_POINTS = 1000000
AREA_FACTOR = 4
inside_circle = 0

# Randomly generate points and count those inside the circle
for _ in range(NUM_POINTS):
    x = random.uniform(-RADIUS, RADIUS)
    y = random.uniform(-RADIUS, RADIUS)
    if x**2 + y**2 <= RADIUS**2:
        inside_circle += 1

# Estimate pi based on the number of points inside the circle
est_pi = (inside_circle / NUM_POINTS) * AREA_FACTOR

print(f"Estimated value of pi is: {est_pi}")
