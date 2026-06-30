# Engineering Analysis Toolkit

A Python-based engineering toolkit for performing common mechanical engineering calculations and visualisations.

The toolkit combines multiple engineering analysis modules into a single application, demonstrating structural mechanics, machine design and engineering software development using Python.

---

## Current Modules

- ✅ Beam Deflection Analysis
- ✅ Shaft Stress Analysis
- ✅ Mohr's Circle Visualiser
- ✅ Euler Buckling Analysis

---

## Features

- Interactive command-line application
- User-defined engineering inputs
- Automatic graph generation
- High-resolution image export
- Engineering calculations
- Modular Python architecture

---

## Technologies Used

- Python
- NumPy
- Matplotlib

---

## Project Structure

```text
engineering-analysis-toolkit/

│── beam_deflection.py
│── shaft_stress_analysis.py
│── mohrs_circle.py
│── buckling_analysis.py
│── main.py
│── images/
│── README.md
```

---

## Running the Toolkit

Run the main application:

```bash
python main.py
```

You will then see:

```text
========================================
      ENGINEERING ANALYSIS TOOLKIT
========================================

1. Beam Deflection Analysis
2. Shaft Stress Analysis
3. Mohr's Circle
4. Buckling Analysis
5. Exit
```

Select a module by entering its corresponding number.

Each module prompts the user for the required engineering parameters before performing the calculations and displaying the results.

---

## Module Overview

### Beam Deflection Analysis

Calculates and plots the deflection of a simply supported beam subjected to a central point load.

### Shaft Stress Analysis

Calculates the shear stress distribution across a circular shaft subjected to torsion.

### Mohr's Circle

Visualises the stress state, principal stresses and maximum shear stress using Mohr's Circle.

### Euler Buckling Analysis

Calculates the Euler critical buckling load for several common column end conditions and compares them graphically.

---

## Example Outputs

The generated figures are automatically saved inside the `images` folder for documentation and future reference.

---

## Future Development

- Torsion Analysis
- Pressure Vessel Analysis
- Fatigue Analysis
- Heat Transfer Calculator
- Fluid Flow Calculator
- Unit Conversion Utilities
- PDF Report Generation
- Graphical User Interface (GUI)

---

## Author

Created as part of a professional mechanical engineering software portfolio demonstrating engineering analysis, numerical computing and Python application development.
