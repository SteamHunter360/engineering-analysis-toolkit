import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

# Shaft properties
diameter = float(input("Enter shaft diameter (m): "))
torque = float(input("Enter applied torque (N·m): "))

# Radius values
r = np.linspace(0, diameter / 2, 200)

# Polar second moment of area
J = (np.pi * diameter**4) / 32

# Shear stress distribution
tau = (torque * r) / J

# Plot
plt.figure(figsize=(8, 5))

plt.plot(r * 1000, tau / 1e6, linewidth=2)

plt.title("Shear Stress Distribution in a Circular Shaft")
plt.xlabel("Radius (mm)")
plt.ylabel("Shear Stress (MPa)")
plt.grid(True)

plt.savefig("images/shaft_stress_distribution.png", dpi=300)

maximum_shear = np.max(tau)

print(f"Maximum Shear Stress = {maximum_shear / 1e6:.2f} MPa")

plt.show()