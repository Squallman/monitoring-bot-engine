import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zakaz_ua",
    version="0.0.1",
    author="Serhii Shepel",
    author_email="serhiy.shepel@gmail.com",
    description="Small module to work with zakaz ua slots",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Squallman/zakaz-ua",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
