from setuptools import setup, find_packages

PACKAGE="Ext-A"
VERSION="0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="""Ext-A extension for Review Board""",
    author="Mike Conley",
    packages=["exta"],
    entry_points={
        'reviewboard.extensions':
        '%s = exta.extension:ExtAExtension' % PACKAGE,
    },
    package_data={
        'exta': [
            'htdocs/css/*.css',
            'htdocs/js/*.js',
            'templates/exta/*.html',
            'templates/exta/*.txt',
        ],
    }
)


