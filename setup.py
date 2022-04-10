from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as f:
        return f.read()

setup(
    name="my_local_api",
    version=VERSION,
    description="Creates a local api",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="api",
    url="https://github.com/danilocgsilva/my_local_api",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["my_local_api"],
    entry_points={"console_scripts": ["mylocalapi=my_local_api.__main__:main"],},
    include_package_data=True
)

