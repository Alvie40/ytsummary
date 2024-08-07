from Cython.Build import cythonize
from setuptools import setup

setup(
    name='ytsummary',
    ext_modules=cythonize('ytsummary/__init__.py'),
    zip_safe=False,
)
