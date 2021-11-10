
from setuptools import setup, find_packages
from osdelimport.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='osdelimport',
    version=VERSION,
    description='Import books from OSDEL to eshops',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Sotirios Oikonomou',
    author_email='sotoik@gmail.com',
    url='https://github.com/sotiris-oikonomou/osdelimport',
    license='GNU General Public License v3.0',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'osdelimport': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        osdelimport = osdelimport.main:main
    """,
)
