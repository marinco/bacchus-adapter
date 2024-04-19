from setuptools import setup

from adapter import __version__

setup(
    name='bacchus-adapter',
    version=__version__,
    packages=['adapter', 'adapter.util'],
    url='https://github.com/marinco/bacchus-adapter',
    license='',
    author='Marin Milina',
    author_email='marin.milina96@gmail.com',
    description='Converter for poor Bacchus 3 PDF exports'
)
