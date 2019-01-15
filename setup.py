from setuptools import setup

test_req = ['pytest==4.0.2', ]
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='pypkgfreeze',
    version='0.1',
    packages=['src'],
    author="Adam Goldschmidt",
    author_email="adamgold7@gmail.com",
    description="Automatically inserts your currently used package versions to setup.py.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adamgold/pypkgfreeze",
    install_requires=[
        "Click==7.0",
    ],
    tests_require=test_req,
    setup_requires=['pytest-runner==4.2'],
    extras_require={
        'test': test_req
    },
    entry_points={'console_scripts': "pkgfreeze=src.pypkgfreeze:main"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: BSD License",
    ],
)
