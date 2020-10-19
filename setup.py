from distutils.core import setup, Extension
from Cython.Build import cythonize


basics_module = Extension(
    'testpygeos',
    sources=[
        'testpygeos/geos_cpp.pyx', #'inmemscop/printf_voidasd.cpp'
    ],
    libraries=['geos'],  # better to use C library, C++ as for now
    language='c++',  # TODO: probably dont need C++
)



setup(
    name='testpygeos',
    packages=['testpygeos'],
    ext_modules=cythonize(
        basics_module,
        force=True,
        compiler_directives={'language_level' : "3"}
    ),
)