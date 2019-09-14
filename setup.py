from setuptools import setup

setup(
    name="cmdline-nimgex",
    version="0.1.0",
    author="Damien Marlier",
    author_email="damien.marlier@hotmail.fr",
    packages=["nimgex"],
    entry_points={
        "console_scripts": ['nimgex = nimgex.cli:main']
    },
    zip_safe=False
)
