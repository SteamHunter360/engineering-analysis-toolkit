import numpy as np
import matplotlib.pyplot as plt
import os

os.makedirs("images", exist_ok=True)

# Column/material properties
E = 200e9          # Young's modulus, Pa
I = 8e-6           # Second moment of area, m^4
L = 2.0            # Column length, m

# Effective length factors
end_conditions = {
    "Pinned-Pinned": 1.0,
    "Fixed-Free": 2.0,
    "Fixed-Pinned": 0.7,
    "Fixed-Fixed": 0.5
}

critical_loads = {}

for condition, K in end_conditions.items():
    P_cr = (np.pi**2 * E * I) / ((K * L) ** 2)
    critical_loads[condition] = P_cr

print("\nEuler Buckling Critical Loads:\n")

for condition, load in critical_loads.items():
    print(f"{condition}: {load / 1000:.2f} kN")

# Plot
plt.figure(figsize=(8, 5))

plt.bar(
    critical_loads.keys(),
    [load / 1000 for load in critical_loads.values()]
)

plt.title("Euler Buckling Critical Load by End Condition")
plt.xlabel("End Condition")
plt.ylabel("Critical Load (kN)")
plt.grid(axis="y")

plt.tight_layout()
plt.savefig("images/buckling_analysis.png", dpi=300)

plt.show()