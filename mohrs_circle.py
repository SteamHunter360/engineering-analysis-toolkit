import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

# Stress state (MPa)
sigma_x = 80
sigma_y = 20
tau_xy = 30

# Centre and radius
centre = (sigma_x + sigma_y) / 2

radius = np.sqrt(
    ((sigma_x - sigma_y) / 2) ** 2
    + tau_xy ** 2
)

theta = np.linspace(
    0,
    2 * np.pi,
    300
)

sigma = centre + radius * np.cos(theta)
tau = radius * np.sin(theta)

plt.figure(figsize=(6,6))

plt.plot(sigma, tau, linewidth=2)

plt.scatter(
    [sigma_x, sigma_y],
    [tau_xy, -tau_xy],
    label="Original Stress State"
)

plt.scatter(
    [centre + radius, centre - radius],
    [0,0],
    label="Principal Stresses"
)

plt.axhline(0, color="black")
plt.axvline(0, color="black")

plt.grid(True)

plt.axis("equal")

plt.title("Mohr's Circle")

plt.xlabel("Normal Stress (MPa)")
plt.ylabel("Shear Stress (MPa)")

plt.legend()

plt.savefig(
    "images/mohrs_circle.png",
    dpi=300
)

print(f"Principal Stress 1 = {centre + radius:.2f} MPa")
print(f"Principal Stress 2 = {centre - radius:.2f} MPa")
print(f"Maximum Shear Stress = {radius:.2f} MPa")

plt.show()