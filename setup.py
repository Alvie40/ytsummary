from setuptools import setup
from Cython.Build import cythonize

setup(
    name='ytsummary',
    ext_modules=cythonize("ytsummary/__init__.py"),
    zip_safe=False,
)
