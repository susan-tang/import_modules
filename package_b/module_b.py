# from package_a.module_a import something
# from ..package_a.module_a import something
import sys

print('before', sys.path)
sys.path.append("../package_a")
print('after', sys.path)

from package_a.module_a import something # not working

print(something)