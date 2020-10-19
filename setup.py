from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy



extensions = [
    Extension(
        'testgeos_cpp',
        ['testgeos/geos_cpp.pyx'],
        libraries=['geos'],
        language='c++',
    ),
    Extension(
        'testgeos_pygeos',
        ['testgeos/pygeos_raw.pyx'],
    ),
    Extension(
        'testgeos_pygeos_c',
        ['testgeos/pygeos_c.pyx'],
        libraries=['geos_c']        
    ),
]





setup(
    name='testgeos',
    # packages=['testpygeos'],
    ext_modules=cythonize(
        extensions,
        force=True,
        compiler_directives={'language_level' : "3"}
    ),
)