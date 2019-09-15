from setuptools import setup

setup(
    name="junix",
    version="0.1.0",
    author="Damien Marlier",
    author_email="damien.marlier@hotmail.fr",
    description="Simple library to export images from Jupyter notebook",
    packages=["junix"],
    entry_points={
        "console_scripts": ['junix = junix.cli:main']
    }
)
