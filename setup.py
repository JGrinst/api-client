import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

with open("requirements.txt", "r") as requirements_file:
    requirements = requirements_file.read()

setuptools.setup(
    name = "gro",
    version = "1.0.0",
    description = "Python client library for accessing Gro Intelligence's agriculture data platform",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/gro-intelligence/api-client",
    packages = [ 'api' ],
    py_modules = [ 'api.client', 'api.client.lib' ],
    python_requires = ">=2.7.6",
    install_requires = requirements,
    entry_points = {
      'console_scripts': ['gro=api.client.gro_client:main']
    }
)