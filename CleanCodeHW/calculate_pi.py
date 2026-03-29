import random
# Constant settings
RADIUS = 1
NUM_POINTS = 1000000
SQ_AREA = (RADIUS * 2) ** 2
inside_circle = 0

# Randomly generate points and count those inside the circle
for _ in range(1000000):
    x = random.uniform(-RADIUS, RADIUS)
    y = random.uniform(-RADIUS, RADIUS)
    if x**2 + y**2 <= RADIUS**2:
        inside_circle += 1

# Estimate pi based on the number of points inside the circle
est_pi = (inside_circle / NUM_POINTS) * SQ_AREA

print(f"Estimated value of pi is: {est_pi}")
