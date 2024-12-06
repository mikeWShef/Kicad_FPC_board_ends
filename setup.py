import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="kicad_fpc_footprint_generator",
    version="0.0.1",
    author="Mike Watson",
    author_email="m.watson@rivelinrail.com",
    description=("A command line program to generate FPC board end footprints in kicad format"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mikeWShef/Kicad_FPC_board_ends",
    project_urls={
        "Bug Tracker": "https://github.com/mikeWShef/Kicad_FPC_board_ends/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Unlicence",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "fpc_footprint_generator = kicad_fpc_footprint_generator.cli:main",
        ]
    }
)