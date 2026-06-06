import sys
import os

# Make local package override any installed version
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import ultimateraylib as rl
from ultimateraylib import rlgl
