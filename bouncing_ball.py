import numpy as np
from matplotlib import pyplot as plt


class Ball:
    def __init__(self, density: float, restitution: float, colour: str, name: str, radius: float):
        self.density = density
        self.restitution = restitution
        self.colour = colour  # Colour that trajectory line will appear on graph
        self.name = name
        self.radius = radius


while True:
    try:
        n = int(input("Enter fluid number (1 = glycerine, 2 = water, 3 = air): ")) - 1
        break
    except ValueError:
        print("Invalid input. Please enter a number.")

FLUIDS = [1260, 1000, 1.225]  # Fluid densities
C_D = 0.5  # Drag coefficient
DT = 0.001  # Time step
G = -9.81  # Gravitational constant
T_MAX = 10  # End time

nylon = Ball(1140, 0.8, "r", "Nylon", 0.0025)
steel = Ball(7850, 0.6, "b", "Steel", 0.0025)
ball_list = [nylon, steel]

for ball in ball_list:
    # Initial conditions
    time = 0
    y_vel = 0
    y_pos = 5  # Height ball is dropped from

    y_pos_list = [y_pos]
    y_vel_list = [y_vel]
    time_list = [time]

    restitution_coeff = ball.restitution
    mass = ((4 / 3) * np.pi * ball.radius ** 3) * ball.density
    area = ball.radius ** 2 * np.pi

    while time <= T_MAX:
        time = time + DT

        # Drag equation: np.abs() used to preserve vector property
        drag = 0.5 * FLUIDS[n] * y_vel * np.abs(y_vel) * C_D * area

        buoyancy = -1 * FLUIDS[n] * ((4 / 3) * np.pi * ball.radius ** 3) * G

        # Determine whether ball will bounce
        if y_pos <= 0:
            y_vel = restitution_coeff * np.abs(y_vel)  # Ball bounces
        else:
            y_vel = y_vel + ((mass * G - drag + buoyancy) / mass) * DT  # Newton's second law of motion

        y_pos = y_pos + y_vel * DT

        y_pos_list.append(y_pos)
        time_list.append(time)
        y_vel_list.append(y_vel)

    print(f"Maximum velocity (m/s) reached by {ball.name} ball: {np.abs(np.min(y_vel_list))}")
    plt.plot(time_list, y_pos_list, ball.colour, label=ball.name)

plt.grid(True)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title(f"Ball trajectories over {T_MAX} seconds in fluid {n + 1}")
plt.legend()
plt.show()
