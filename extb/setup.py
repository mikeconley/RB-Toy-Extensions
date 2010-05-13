from setuptools import setup, find_packages

PACKAGE="Ext-B"
VERSION="0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="""Ext-B extension for Review Board""",
    author="Mike Conley",
    packages=["extb"],
    entry_points={
        'reviewboard.extensions':
        '%s = extb.extension:ExtBExtension' % PACKAGE,
    },
    package_data={
        'extb': [
            'htdocs/css/*.css',
            'htdocs/js/*.js',
            'templates/extb/*.html',
            'templates/extb/*.txt',
        ],
    }
)


