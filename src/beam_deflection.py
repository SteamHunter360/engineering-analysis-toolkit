import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

# Beam properties
L = float(input("Enter beam length L (m): "))
P = float(input("Enter centre point load P (N): "))
E = float(input("Enter Young's modulus E (Pa): "))
I = float(input("Enter second moment of area I (m^4): "))
x = np.linspace(0, L, 200)

# Simply supported beam with centre point load
y = (P * x * (L**3 - 2 * L * x**2 + x**3)) / (48 * E * I)

plt.figure(figsize=(10,5))

plt.plot(x, y * 1000)

plt.title("Beam Deflection")
plt.xlabel("Beam Length (m)")
plt.ylabel("Deflection (mm)")
plt.grid(True)

print(f"Maximum deflection = {max(y)*1000:.3f} mm")

plt.savefig("images/beam_deflection.png", dpi=300)

plt.show()