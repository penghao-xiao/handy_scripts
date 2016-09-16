#!/usr/bin/env python

'''
rotate a structure to satisfy the ssneb requirements:
cell[0] along the x axis and cell[1] on the xoy plane
'''
from ase.io import read,write
import sys

finput = sys.argv[1]
p1 = read(finput,format='vasp')
a = p1.get_cell()
print a[0]
p1.rotate(a[0],'x',center=(0,0,0),rotate_cell=True)
a = p1.get_cell()
b = a[1]
b[0] = 0.0
p1.rotate(b,'y',center=(0,0,0),rotate_cell=True)

write(finput+'_rotated',p1,format='vasp')
