import sys
from setuptools import setup

from utilitiespackagemlmetapackage.settings import *

assert sys.version_info >= MINIMUM_PYTHON_VERSION

setup(
    name="utilities-package_ml-metapackage",
    version=VERSION,
    description="utilities package ml metapackage",
    url="https://github.com/terminal-labs/utilities-package_ml-metapackage",
    author="Terminal Labs",
    author_email="solutions@terminallabs.com",
    license="see LICENSE file",
    packages=["utilitiespackagemlmetapackage"],
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "setuptools",
        "click",
        "black",
        "flake8",
    ],
    entry_points="""
        [console_scripts]
        utilitiespackagemlmetapackage=utilitiespackagemlmetapackage.__main__:main
    """,
)
