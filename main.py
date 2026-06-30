import subprocess

while True:

    print("\n==============================")
    print(" Engineering Analysis Toolkit")
    print("==============================")

    print("1. Beam Deflection")
    print("2. Shaft Stress Analysis")
    print("3. Mohr's Circle")
    print("4. Buckling Analysis")
    print("5. Exit")

    choice = input("\nSelect Module: ")

    if choice == "1":
        subprocess.run(["python", "beam_deflection.py"])

    elif choice == "2":
        subprocess.run(["python", "shaft_stress_analysis.py"])

    elif choice == "3":
        subprocess.run(["python", "mohrs_circle.py"])

    elif choice == "4":
        subprocess.run(["python", "buckling_analysis.py"])

    elif choice == "5":
        break

    else:
        print("Invalid Selection")