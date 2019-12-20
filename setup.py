from setuptools import find_packages
from setuptools import setup

setup(
    name='fantastic_spork',
    version='0.1',
    url='https://github.com/victoriademina/fantastic-spork',
    license='Apache-2.0',
    author='Victoria Demina',
    author_email='viktoriia.demina@gmail.com',
    description='',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.7',
    install_requires=[],
    extras_require={
        'dev': [
            'pytest',
            'tox',
        ],
    },
)
