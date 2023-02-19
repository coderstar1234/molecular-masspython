#Created By Lamron

"""
Before you use it, there is a format you have to follow:

1. Each Element has to be separated by space character and a plus sign

2. Each Element can only have a coefficient ranging from 1(included) to 10(excluded)

3. Each Coefficient must come before the Element and there is no need to separate them.

4. All elements must be written as they are presented in the periodic table. e.g. 'O' instead of 'o', 'Mg' instead of 'MG' or 'mg' or 'Magnesium'

Examples:
3N + 2O
7Cl + 2Na

"""

element_masses = {
'H': 1.008, 'He': 4.003, 'Li': 6.941, 'Be': 9.012, 'B': 10.81, 'C': 12.01, 'N': 14.01, 'O': 16.0, 'F': 19.0, 'Ne': 20.18, 'Na': 22.99, 'Mg': 24.31, 'Al': 26.98, 'Si': 28.09, 'P': 30.97, 'S': 32.06, 'Cl': 35.45, 'K': 39.1, 'Ca': 40.08, 'Sc': 44.96, 'Ti': 47.87, 'V': 50.94, 'Cr': 52.0, 'Mn': 54.94, 'Fe': 55.85, 'Ni': 58.69, 'Co': 58.93, 'Cu': 63.55, 'Zn': 65.38, 'Ga': 69.72, 'Ge': 72.63, 'As': 74.92, 'Se': 78.96, 'Br': 79.9, 'Kr': 83.8, 'Rb': 85.47, 'Sr': 87.62, 'Y': 88.91, 'Zr': 91.22, 'Nb': 92.91, 'Mo': 95.94, 'Tc': 98.0, 'Ru': 101.07, 'Rh': 102.91, 'Pd': 106.42, 'Ag': 107.87, 'Cd': 112.41, 'In': 114.82, 'Sn': 118.71, 'Sb': 121.76, 'I': 126.9, 'Te': 127.6, 'Xe': 131.29, 'Cs': 132.91, 'Ba': 137.33, 'La': 138.91, 'Ce': 140.12, 'Pr': 140.91, 'Nd': 144.24, 'Pm': 145.0, 'Sm': 150.36, 'Eu': 151.96, 'Gd': 157.25, 'Tb': 158.93, 'Dy': 162.5, 'Ho': 164.93, 'Er': 167.26, 'Tm': 168.93, 'Yb': 173.05, 'Lu': 175.0, 'Hf': 178.49, 'Ta': 180.95, 'W': 183.84, 'Re': 186.21, 'Os': 190.23, 'Ir': 192.22, 'Pt': 195.08, 'Au': 196.97, 'Hg': 200.59, 'Tl': 204.38, 'Pb': 207.2, 'Bi': 209.0}
#asking AI to generate a dictionary with atomic masses

new_masses = {} #new dictionary

for key, value in element_masses.items():
    new_masses[key] = round(value)
#loop through the list to change the masses from float to int    

print('Please enter an equation:') #asking for equation
a = input()
print(a)

b = a.split(' ') #making a list by splitting the equation.

molecular_mass = 0

print()

for x in b: #loop through each component of the list
    for y in x: #loop through each character of the component
        if y.isdigit(): #if character is a digit it will do the following:
            print(f'{y} lots of {x[1:]} - Total atomic mass is: {new_masses[x[1:]]} * {int(y)} = {new_masses[x[1:]]*int(y)} grams\n') #created by Lamron
            molecular_mass += new_masses[x[1:]]*int(y)
    if x in new_masses: #another condition where there are no coefficients in a component
        print(f'The element is: {x} - Atomic mass of an element is: {new_masses[x]} grams\n')
        molecular_mass += new_masses[x]
    else: #created by Lamron
        continue #if nothing meets the requirements just continue
   
print('The molecular mass is:', molecular_mass,'grams') #total printed at the end