from distutils.core import setup
from distutils.extension import Extension

setup(name='middleground',
      version='0.1',
      description='middleground is a Python module for converting various document types to a normalised plaintext using am Apache Tika server.',
      packages=['middleground'],
      install_requires=[
          'ezodf',
          'html2text',
          'odfpy',
          'pdfminer3k',
          'ply',
          'py',
          'pytest',
          'wheel',
          'xlrd'
      ])
