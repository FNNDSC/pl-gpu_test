from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'gpu_test',
    version          = '1.0.1',
    description      = 'An app to check GPU availability',
    long_description = readme,
    author           = 'Sandip Samal',
    author_email     = 'sandip.samal@childrens.harvard.edu',
    url              = 'https://github.com/FNNDSC/pl-pfdicom_tagSub',
    packages         = ['gpu_test'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'gpu_test = gpu_test.__main__:main'
            ]
        }
)