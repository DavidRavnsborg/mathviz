import os
import sys

""" This file can be imported to give vignettes access to the mathviz subfolder. """

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import mathviz
