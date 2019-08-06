from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="bdist_wheel_name",
    version="0.1.0",
    description="Generate the name that bdist_wheel would use",
    long_description=long_description,
    # The project's main homepage.
    url="https://github.com/davidszotten/bdist_wheel_name",
    # Choose your license
    license="MIT",
    py_modules=["bdist_wheel_name"],
    install_requires=["wheel"],
    entry_points={"distutils.commands": ["bdist_wheel_name=bdist_wheel_name:bdist_wheel_name"]},
)
