from distutils import extension
from distutils.core import setup, Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext



extensions = [
    Extension(
        'testgeos_cpp',
        ['testgeos/geos_cpp.pyx'],
        libraries=['geos'],
        language='c++',
    ),
    Extension('testgeos_pygeos',
        ['testgeos/pygeos_f.pyx'],
    )
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