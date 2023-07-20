from setuptools import setup, find_packages
import os
import io


with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), 'httpbin', 'VERSION')) as version_file:
    version = version_file.read().strip()

setup(
    name="httpbin",
    version=version,
    description="HTTP Request and Response Service",
    long_description="A simple HTTP Request & Response Service, written in Python + Flask.",

    # The project URL.
    url='https://github.com/requests/httpbin',

    # Author details
    author='Kenneth Reitz, Phil Huang',
    author_email='me@kennethreitz.org, phil.huang@microsoft.com',

    # Choose your license
    license='ISC',

    classifiers=[
         'Development Status :: 5 - Production/Stable',
         'Intended Audience :: Developers',
         'Natural Language :: English',
         'License :: OSI Approved :: ISC License (ISCL)',
         'Programming Language :: Python',
         'Programming Language :: Python :: 3.10',
    ],
    test_suite="test_httpbin",
    packages=find_packages(),
    include_package_data = True, # include files listed in MANIFEST.in
    install_requires=[
        'Flask', 'MarkupSafe', 'decorator', 'itsdangerous', 'six', 'brotlipy',
        'raven[flask]', 'werkzeug>=0.14.1', 'gevent', 'flasgger'
    ],
)
