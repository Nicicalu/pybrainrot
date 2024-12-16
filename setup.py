from setuptools import setup
from pybrainrot import VERSION_NUMBER

with open("README.md", "r") as fh:
    long_description = fh.read()

# Install python package, scripts and manual pages
setup(name="pybrainrot",
      version=VERSION_NUMBER,
      author="Nicolas Caluori",
      author_email="brainrot@nicolas-caluori.ch",
      license="MIT",
      description="Python with rizz",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/nicicalu/pybrainrot",
      scripts=["scripts/brainrot2py", "scripts/pybrainrot", "scripts/py2brainrot"],
      packages=["pybrainrot"],
      zip_safe=False)