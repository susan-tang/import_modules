# from package_a.module_a import something  # it's working
# import package_a.module_a as a_module # it's working
from package_a import module_a as a_module # it's working
# from .package_a.module_a import something # ImportError: attempted relative import with no known parent package

# print(something)
# print(a_module.something)