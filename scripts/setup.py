import os

import pkg_resources
from setuptools import setup, find_packages


def read_version(fname="version.py"):
    exec(compile(open(fname, encoding="utf-8").read(), fname, "exec"))
    return locals()["__version__"]


setup(
    name="youtube",
    version="0.1.0",
    description="Youtube Helper",
    python_requires=">=3.7",
    author="Maslax Ali",
    url="https://github.com/alimaslax/audio-ai",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": ["youtube=youtube.yt:main"],
    },
    include_package_data=True,
    extras_require={"dev": ["pytest"]},
)
