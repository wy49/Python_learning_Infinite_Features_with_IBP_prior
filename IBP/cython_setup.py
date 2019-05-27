from distutils.core import setup
from Cython.Build import cythonize
#ext_modules = cythonize("cython_functions.pyx")
setup(
  #name = 'MyProject',
  #ext_modules = cythonize(["*.pyx"]),
    ext_modules = cythonize("cython_functions.pyx"),
)