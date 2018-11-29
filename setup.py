from setuptools import setup

requires = [
    'python-dateutil>=2.7.5',
]

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='dateutil-br',
    version='0.0.2',
    description='Implementation to Pt-br of python lib python-dateutil',
    long_description=readme,
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
