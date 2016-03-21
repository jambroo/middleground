from distutils.core import setup
from setuptools import setup, find_packages

setup(name='middleground',
      version='0.1',
      description='middleground is a Python module for converting various '+
        'document types to a normalised plaintext using am Apache Tika server.',
      packages=find_packages(),
      install_requires=[
        'docx',
        'ezodf',
        'html2text',
        'lxml',
        'odfpy',
        'pdfminer3k',
        'Pillow',
        'ply',
        'py',
        'pytest',
        'requests',
        'tika',
        'wheel',
        'xlrd'
      ])
