#!/usr/bin/python3

# This is the jsnpath "step" library.

# --------------------------------------- FUNCTIONS
def matches(stepexpression, typedef):


# INTERNAL
def matchesnumberstep(expr):



# --------------------------------------- CONSTANTS

# general steps 

wildcard_index_pattern = '(' + '\[\]' + ')'

numpattern = '-?[0-9]+'

single_index_pattern = '(' + numpattern + ')'

slicepattern = '((' + numpattern + ')[:])'
slicepattern += '|'
slicepattern += '([:](' + numpattern + '))'
slicepattern += '|'
slicepattern += '((' + numpattern + ')[:](' + numpattern + '))'

indexpattern = wildcard_index_pattern + '|' 
    + '(' + '\[(' + single_index_pattern + '|' 
    + slicepattern + ')\]' + ')'

