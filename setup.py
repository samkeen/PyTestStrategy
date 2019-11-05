import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyTestStrategy_sam-keen",
    version="0.0.1",
    author="Sam Keen",
    author_email="sam.sjk@gmail.com",
    description="Template for testing strategy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/samkeen/PyTestStrategy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)