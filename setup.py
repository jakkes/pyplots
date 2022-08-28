import pathlib
import setuptools

HERE = pathlib.Path(__file__).parent

with open(HERE / "README.md", "r") as fh:
    long_description = fh.read()

with open(HERE / "VERSION", "r") as f:
    version = f.read()

setuptools.setup(
    name="pyplots",
    version=version,
    author="Jakob Stigenberg",
    description="Wraps matplotlib for easier plotting.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jakkes/pyplots",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    python_requires=">=3.7",
    install_requires=["matplotlib~=3.4.3"]
)

### Publish
### python3 setup.py sdist bdist_wheel
### twine upload dist/*