from setuptools import setup, find_namespace_packages

setup(
    name="ur",
    version="0.1.0",
    license="BSD-2-Clause Plus Patent License",
    url="https://github.com/Foundation-Devices/foundation-ur-py",
    description="UR Implementation in Python -- ported from the C++ Reference Implementation by Blockchain Commons",
    author="Ken Carpenter",
    author_email="ken@foundationdevices.com",
    packages=find_namespace_packages("src", include=["*"]),
    package_dir={"": "src"},
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
