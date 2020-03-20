from distutils.core import setup
setup(
  name = 'superstring',
  packages = ['superstring'],
  version = '0.2',
  license='MIT',
  description = 'A fast and memory-optimized string library for heavy-text manipulation',
  author = 'Wael Boutglay',
  author_email = 'btwael@gmail.com',
  url = 'https://github.com/btwael/superstring.py',
  download_url = 'https://github.com/btwael/superstring.py/archive/superstring.py_0.2.tar.gz',
  keywords = ['string', 'rope', 'memory-optimized'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
