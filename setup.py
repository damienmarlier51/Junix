from setuptools import setup

setup(
    name="junix",
    version="0.2.0",
    author="Damien Marlier",
    author_email="damien.marlier@hotmail.fr",
    description="Simple library to export images from Jupyter notebook",
    packages=["junix"],
    install_requires=['img2pdf>=0.4'],
    entry_points={
        "console_scripts": ['junix = junix.cli:main']
    }
)
