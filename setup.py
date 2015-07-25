from os import path
from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='table2dicts',
    version='0.1b',
    description='Parse and split PEM files painlessly.',
    long_description=(read('README.rst')),
    url='http://github.com/moagstar/table2dicts/',
    download_url = 'https://github.com/moagstar/table2dicts/tarball/0.1b',
    license='MIT',
    author='Daniel Bradburn',
    author_email='moagstar@gmail.com',
    py_modules=['table2dicts'],
    include_package_data=True,
    install_requires = ['BeautifulSoup4'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
