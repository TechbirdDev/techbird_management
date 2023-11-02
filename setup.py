from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in techbird_management/__init__.py
from techbird_management import __version__ as version

setup(
	name="techbird_management",
	version=version,
	description="Techbird Management modules",
	author="Tech bird",
	author_email="amol@techbirdit.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
