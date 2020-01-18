# Check versions of the components of the Python stack

'''
If you already have miniconda or anaconda installed,
then execute the following two commands to update package versions to the latest

% conda update conda
% conda update python jupyter numpy scipy pandas matplotlib scikit-learn

'''

fmt = "%15s: %s"

#Python
# import sys
# print( fmt % ("Python", sys.version))

aid = input("Please enter your AndrewID: ")

# Below requests extension courtesy of Devansh Kukreja, S19 364 TA

try:
	import requests
	r = requests.get('https://apis.scottylabs.org/directory/v1/andrewID/'+aid)
	aid = r.json()['first_name']
except:
	pass

print("\n* Welcome to the course, %s!\n" % aid)
print("Your Python environment is:\n ")

import platform
print( fmt % ("Python", platform.python_version()))

#IPython is what you are using now to run the notebook
import IPython
print( fmt % ("IPython", IPython.__version__ ))

# Numpy is a high performance library for working with Arrays
import numpy as np
print( fmt % ("Numpy", np.__version__ ))

# SciPy implements many different numerical algorithms
import scipy as sp
print( fmt % ("Scipy", sp.__version__ ))

# Pandas makes working with data tables easier
import pandas as pd
print( fmt % ("Pandas", pd.__version__ ))

# Module for plotting
import matplotlib
print( fmt % ("Matplotlib", matplotlib.__version__ ))

# Extensions to matplotlib
import seaborn as sns
print( fmt % ("Seaborn", sns.__version__ ))

# SciKit Learn implements several Machine Learning algorithms
import sklearn
print( fmt % ("Scikit-learn", sklearn.__version__ ))

print()
