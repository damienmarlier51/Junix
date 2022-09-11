from setuptools import setup

setup(
    name="junix",
    version="0.1.5",
    author="Damien Marlier",
    author_email="damien.marlier@hotmail.fr",
    description="Utils to export images from Jupyter notebook",
    packages=["junix"],
    entry_points={"console_scripts": ["junix = junix.cli:export_images"]},
    install_requires=[
        "click",
    ],
)
