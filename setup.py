import setuptools

from distutils.core import setup
setup(
  name = 'imgcompare',
  packages = ['imgcompare'],
  version = '0.1.0',
  description = 'compares two images for equality or a difference percentage',
  author = 'Jonas Hahn',
  author_email = 'jonas.hahn@datenhahn.de',
  url = 'https://github.com/datenhahn/imgcompare',
  download_url = 'https://github.com/datenhahn/imgcompare/tarball/0.1.0',
  keywords = ['image', 'compare'],
  classifiers = [],
  license='MIT',
  install_requires=['pillow']
)