from setuptools import setup

requires = [
    'dateutil==*',
]

setup(
    name='dateutilbr',
    version='1.0.0',
    description='IMplementation to Pt-br of python lib python-dateutil',
    url='http://github.com/magrathealabs/dateutil-br',
    author='Magrathea Labs',
    author_email='contact@magrathealabs.com',
    license='MIT',
    packages=['dateutilbr', 'dateutilbr/github'],
    zip_safe=False,
    keywords = ['date parser python', 'date parser', 'dateutil', 'data em português'],
    install_requires=requires,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2 :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
