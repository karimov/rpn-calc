import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rpn-calc",
    version="0.0.1",
    author="Davron Sh. Karimov",
    author_email="d.karimov@unicon.uz",
    description="A small rpn calculator in a unix-like command line tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://git.unicon.uz/davron/rpc-calc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'rpn = rpn.run:main'
        ]}
)
