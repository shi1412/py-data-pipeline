from setuptools import setup
from jobs.version import VERSION

description='A library for transaction processing: getting data feed and transform into analytic format'
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError, RuntimeError):
    long_description = description

setup(
    name='pyoltp',
    packages=['pyoltp'],
    version=VERSION,
    description=description,
    long_description=long_description,
    author='Michael Shi',
    url='https://github.com/shi1412/pyspark-oltp-pipeline',
    keywords=['pyspark', 'fault-tolerant', 'oltp', 'data-preparation', 'data-exploration'],
    install_requires=['pyspark==2.4.5', 'tweepy==3.10.0'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'console_scripts': [
           
        ],
    },
)