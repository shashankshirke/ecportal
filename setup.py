from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ecportal/__init__.py
from ecportal import __version__ as version

setup(
	name="ecportal",
	version=version,
	description="EC Portal (Production)",
	author="Esycommerce",
	author_email="admin@esycommerce.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
