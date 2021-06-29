import sys
sys.path.append('../../../../../')

from simple_nn_v2 import simple_nn
from simple_nn_v2.init_inputs import initialize_inputs
from simple_nn_v2.features.symmetry_function import generating

# Minimum Setting for Testing Symmetry_function methods
# Initialize input file, set Simple_nn object as parent of Symmetry_function object

logfile = open('LOG', 'w', 10)
inputs = initialize_inputs('./input.yaml', logfile)
atom_types = inputs['atom_types']

""" Previous setting before test code

    1. load structure from FILE

"""
from ase import io
########## Set This Variable ###########
FILE = '../../../../test_data/SiO2/OUTCAR_comp'
########################################
structures = io.read(FILE, index='::', format='vasp-out', force_consistent=True)
structure = structures[0]

""" Main test code

    Test _get_structure_info()
    1. check if "atom_num" is total atom number
    2. check "type_num" has correct element types and atom number for each elements
    3. check if atom_type_idx has correct values
    4. check "type_atom_idx" has correct atom index 
    5. check lattice parameter
    6. check Cartesian coordination in "cart" (first 5, last 5 coordination)
    7. check Fractional coordination in "scale" (first 5, last 5 coordination)

"""
import numpy as np

cell, cart, scale= generating._get_structure_coordination_info(structure)
cell_comp = np.copy(structure.cell, order='C')
cart_comp=np.copy(structure.get_positions(wrap=True), order='C')
scale_comp = np.copy(structure.get_scaled_positions(), order='C')

print('1. check lattice parameter')
print('Lattice parameter')
for i in range(3):
    print(cell[i][0], cell[i][1], cell[i][2])
    for j in range(3):
        if cell[i][j] != cell_comp[i][j]:
            print("%s, %s index lattice parameter has wrong values"%(i, j))

print('\n2. check Cartesian coordination in "cart" (first 5, last 5 coordination)')
print('Cartesian coordination')
for i in range(len(cart)):
    if i <5 or i>=len(cart)-5:
        print cart[i][0], cart[i][1], cart[i][2]
    if i == 5:
        print('...')
    for j in range(3):
        if cart[i][j] != cart_comp[i][j]:
            print("%s th atom's %s th cartesian coordination has wrong values"%(i+1, j))

print('\n3. check Fractional coordination in "cart_p" (first 5, last 5 coordination)')
print('Fractional coordination')
for i in range(len(scale)):
    if i <5 or i>=len(scale)-5:
        print scale[i][0], scale[i][1], scale[i][2]
    if i == 5:
        print('...')
    for j in range(3):
        if scale[i][j] != scale_comp[i][j]:
            print("%s th atom's %s th fractional coordination has wrong values"%(i+1, j))

