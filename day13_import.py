"""
Theory of Import in Python

An import is used to bring modules, packages, or selected names into a Python program.
It allows code to be reused instead of being rewritten.

Common forms:
- import module_name
- from module_name import name
- from module_name import *
- import module_name as alias

Python searches for the imported module in a defined search path, including the
current project directory and installed library locations. Imported modules are
cached in sys.modules, so a module is generally executed only once per interpreter
session. Packages organize related modules using directories and __init__.py files.

Relative imports work within packages, while absolute imports specify the full module
path from the project or library root.
"""
