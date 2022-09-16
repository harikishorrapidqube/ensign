from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in ensign/__init__.py
from ensign import __version__ as version

setup(
	name="ensign",
	version=version,
	description="CRM",
	author="hari.kumar@rapidqube.com",
	author_email="hari.umar@rapidqube.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
