import sys
sys.path.append('../../../../../')
from simple_nn_v2 import simple_nn
from simple_nn_v2.init_inputs import initialize_inputs
from simple_nn_v2.features.symmetry_function import generating
from simple_nn_v2.features.symmetry_function import utils as symf_utils

# Minimum Setting for Testing Symmetry_function methods
# Initialize input file, set Simple_nn object as parent of Symmetry_function object

logfile = open('LOG', 'w', 10)
inputs = initialize_inputs('./input.yaml', logfile)
atom_types = inputs['atom_types']

""" Main test code

Test _parsing_symf_params()
1. Check if 'num' for each elements
2. Check key 'total', 'int', 'double' values for each elements

"""
symf_params_set = symf_utils._parse_symmetry_function_parameters(inputs, atom_types)
print("Check symf_params_set keys")
print(symf_params_set.keys())
print

for elem in symf_params_set.keys():
    print("Check symf_params_set[%s]"%elem)
    print("keys: ", symf_params_set[elem].keys())
    print("['num']: ", symf_params_set[elem]['num'])

    # Check ['total'], ['int'], ['double'] values
    f=open('params_%s'%elem,'r')
    lines=f.readlines()
    f.close()

    tot_e = False
    i_e = False
    d_e = False
    for i, line in enumerate(lines):
        vals = line.split()
        for j in range(len(vals)):
            if float(vals[j]) != symf_params_set[elem]['total'][i][j]:
                print('ValueError in key: total elem: ', elem, '  ', i+1,'th symf, ',j+1, 'th value')
                tot_e = True

            if j<3:
                if float(vals[j]) != symf_params_set[elem]['int'][i][j]:
                    print('ValueError in key: i  elem: ', elem, '  ', i+1,'th symf, ',j+1, 'th value')
                    i_e = True
            elif j>=3:
                if float(vals[j]) != symf_params_set[elem]['double'][i][j-3]:
                    print('ValueError in key: d  elem: ', elem, '  ',i+1,'th symf, ',j+1, 'th value')
                    d_e = True
    if not tot_e:
        print("['total']: ok")
    if not i_e:
        print("['int']: ok")
    if not d_e:
        print("['double']: ok")

    print

