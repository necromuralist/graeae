import sys

if sys.version_info < (3, 0):
    sys.exit(
        ("This doesn't support python 2,"
         " it doesn't support {0}").format(sys.version))

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

setup(name='graeae',
      version='2019.03.10',
      description=("Code to share between the other projects."),
      author="necromuralist",
      platforms=['linux'],
      url='https://github.com/necromuralist/graeae',
      author_email="necromuralist@pm.me",
      install_requires=[
          "bokeh",
          "colorama",
          "holoviews",
          "requests",
          "python-dotenv",
      ]
      packages=find_packages(),
      )
