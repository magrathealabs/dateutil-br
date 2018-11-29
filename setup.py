from setuptools import setup

requires = [
    'python-dateutil==2.7.5',
]

setup(
    name='dateutil-br',
    version='0.0.1',
    description='IMplementation to Pt-br of python lib python-dateutil',
    url='http://github.com/magrathealabs/dateutil-br',
    author='Magrathea Labs',
    author_email='contact@magrathealabs.com',
    license='MIT',
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
