from setuptools import setup, find_packages

PACKAGE="Ext-C"
VERSION="0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="""Ext-C extension for Review Board""",
    author="Mike Conley",
    packages=["extc"],
    entry_points={
        'reviewboard.extensions':
        '%s = extc.extension:ExtCExtension' % PACKAGE,
    },
    package_data={
        'extc': [
            'htdocs/css/*.css',
            'htdocs/js/*.js',
            'templates/extc/*.html',
            'templates/extc/*.txt',
        ],
    },
    install_requires=['Ext-A>=0.1','Ext-B>=0.1']
)


