from setuptools import setup
from os.path import isfile
import os
import io

requires = [
    'python-dateutil>=2.7.5',
]


def README():
    with io.open('README.rst', encoding='utf-8') as f:
        readme_lines = f.readlines()

    # The .. doctest directive is not supported by PyPA
    lines_out = []
    for line in readme_lines:
        if line.startswith('.. doctest'):
            lines_out.append('.. code-block:: python3\n')
        else:
            lines_out.append(line)

    return ''.join(lines_out)


README = README()  # NOQA

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dateutil-br',
    version='0.0.2',
    description='Implementation to Pt-br of python lib python-dateutil',
    long_description=README,
    url='http://github.com/magrathealabs/dateutil-br',
    author='Magrathea Labs',
    author_email='contact@magrathealabs.com',
    license=license,
    packages=['.'],
    zip_safe=False,
    keywords=['date parser python', 'date parser',
              'dateutil', 'dateutil-br', 'data em português'],
    install_requires=requires,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
