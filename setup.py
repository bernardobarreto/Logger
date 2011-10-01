from setuptools import setup, find_packages

readme = open('README.rst').read()
version = "0.0.1"

setup(
    name="logger",
    version="0.0.1",
    license="MIT License",
    author="Bernardo B. Marques",
    author_email="bernardo.fire@gmail.com",
    description="Log your python shell actions",
    url="https://github.com/bernardofire/logger",
    keywords="logger python",
    packages=find_packages(),
    long_description=readme,
    classifiers=[
          'Programming Language :: Python :: 2.6',
          'Topic :: Software Development :: Libraries',
        ],
    )

