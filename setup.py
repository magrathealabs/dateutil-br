import codecs
import os

from setuptools import setup

requires = [
    'python-dateutil>=2.7.5',
]

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

setup(
    name='dateutil-br',
    version='0.0.7',
    description='Implementation to Pt-br of python lib python-dateutil',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/magrathealabs/dateutil-br',
    author='Magrathea Labs',
    author_email='contact@magrathealabs.com',
    license="MIT",
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
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
