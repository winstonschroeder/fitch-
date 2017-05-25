
"""
Importing this module makes all other modules and packages inside this
package available as toplevel modules and packages.
"""

import os
import sys

def install():
    from . import __path__ as path
    sys.path[0:0] = map(os.path.abspath, path)
    del path[:]
