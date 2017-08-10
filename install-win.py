import os
import sys

req = ["pymongo", "opensimplex", "pygame", "pyzmq", "bson", "pykmon", "tmx"]
for dnld in req:
    os.system(sys.exec_prefix + "\\Scripts\\pip3.exe " + dnld)
