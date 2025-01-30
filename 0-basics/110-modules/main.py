# Basically, any .py files are modules and you can import from them
# Python does file name-based imports
import methods as mt # This imports everything from ./methods.py as an object; you can also rename it

mt.print_something()

# Alternatively you can selectively import values from a module
from methods import print_something as ps
ps()

# If you want to organise modules into folders, you need to create a "package"
# Which just means that you need to create a `__init__.py` file in that folder (could just be an empty file)
#  - Note: You don't techinicallt need `__init__.py` to make it work since Python 3.3+, but is the preferred way: https://stackoverflow.com/questions/37139786/is-init-py-not-required-for-packages-in-python-3-3
# Then, you can access its contents using dot notations
from utils.methods import print_something as ps_utils
ps_utils()
