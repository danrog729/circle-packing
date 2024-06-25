import numpy as np
import matplotlib.pyplot as plt

class Circle:
    def __init__(self, x, y, radius=0.5):
        self.x = x
        self.y = y
        self.radius = radius
        self.vx = 0
        self.vy = 0

    def distance_to(self, other):
        return np.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def apply_gravity(self, center_x, center_y, gravity_strength=0.01):
        dx = center_x - self.x
        dy = center_y - self.y
        distance = np.sqrt(dx ** 2 + dy ** 2)
        if distance > 0:
            self.vx += gravity_strength * dx / distance
            self.vy += gravity_strength * dy / distance

    def apply_collision(self, other, collision_strength=0.1):
        distance = self.distance_to(other)
        if distance < 2 * self.radius:
            overlap = 2 * self.radius - distance
            dx = (self.x - other.x) / distance * overlap * collision_strength
            dy = (self.y - other.y) / distance * overlap * collision_strength
            self.vx += dx
            self.vy += dy
            other.vx -= dx
            other.vy -= dy

    def update_position(self):
        self.x += self.vx
        self.y += self.vy
        self.vx *= 0.95  # Damping to reduce oscillations
        self.vy *= 0.95  # Damping to reduce oscillations

def resolve_overlaps(circles):
    for _ in range(100):  # Run several iterations to resolve overlaps
        for i, circle in enumerate(circles):
            for j, other in enumerate(circles):
                if i != j:
                    distance = circle.distance_to(other)
                    if distance < 2 * circle.radius:
                        overlap = 2 * circle.radius - distance
                        dx = (circle.x - other.x) / distance * overlap * 0.5
                        dy = (circle.y - other.y) / distance * overlap * 0.5
                        circle.x += dx
                        circle.y += dy
                        other.x -= dx
                        other.y -= dy

def generate_circle_positions(num_circles, iterations=1000):
    circles = [Circle(np.random.uniform(-5, 5), np.random.uniform(-5, 5)) for _ in range(num_circles)]
    center_x, center_y = 0, 0

    for _ in range(iterations):
        for i, circle in enumerate(circles):
            circle.apply_gravity(center_x, center_y)
            for j, other_circle in enumerate(circles):
                if i != j:
                    circle.apply_collision(other_circle)
        for circle in circles:
            circle.update_position()

    resolve_overlaps(circles)
    
    return [(circle.x, circle.y) for circle in circles]

# Number of circles to pack
num_circles = 250

positions = generate_circle_positions(num_circles)

x_coords, y_coords = zip(*positions)

# Plotting the circles
fig, ax = plt.subplots()
bounding_circle = plt.Circle((0, 0), max(np.sqrt(x**2 + y**2) for x, y in positions) + 0.5, color='r', fill=False)
ax.add_artist(bounding_circle)

for (x, y) in positions:
    circle = plt.Circle((x, y), 0.5, color='b', fill=False)
    ax.add_artist(circle)

ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
ax.set_aspect('equal')
plt.show()

