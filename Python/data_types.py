# LIST -> 1D, 2D, ND arrays
# DICTIONARIES ->  tables
# TUPLES -> 1D arrays that are INMUTABLE
import numpy

sample= [1, ['another', 'list'], ('a', 'tuple')]
print sample[-1], sample[1]

mydictionary= {'potatoes': 2500, 'rijst': 500, 'clothes': 3000}
print mydictionary
mydictionary['potatoes']= 14  # changing one value of the dictionary
print mydictionary
