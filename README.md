<h1 align="center"> Molecular Mass Calculator</h1>

- This is a Python program that calculates the molecular mass of a chemical compound. 
- It takes a chemical formula as input and returns the molecular mass as output.

<h1 align="center">Usage</h1>

- To use this program, simply run the molecular_mass_calculator.py script and input a chemical formula when prompted.
- The program will then calculate the molecular mass and display the result.

bash
Copy code
- python molecular_mass_calculator.py
- Enter a chemical formula: H2O
- The molecular mass of H2O is 18.015 g/mol.
<h1 align="center">Dependencies</h1>

- This program requires the pymatgen library to be installed. You can install it using pip:

Copy code
pip install pymatgen
<h1 align="center">Example</h1>

Here's an example usage of the program:

python
Copy code
from molecular_mass_calculator import calculate_molecular_mass

# Calculate the molecular mass of water
formula = "H2O"
molecular_mass = calculate_molecular_mass(formula)
print(f"The molecular mass of {formula} is {molecular_mass} g/mol.")
This will output:

bash
Copy code
The molecular mass of H2O is 18.015 g/mol.
<h1 align="center">Contributing</h1>

- If you find any bugs or issues with the program, please feel free to open an issue or submit a pull request on GitHub.

<h1 align="center">License</h1>

- This program is licensed under the MIT License. See the LICENSE file for details.
