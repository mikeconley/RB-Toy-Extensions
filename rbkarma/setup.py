from setuptools import setup

PACKAGE="RB-Karma"
VERSION="0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="""RB-Karma extension for Review Board""",
    author="Mike Conley",
    packages=["rbkarma"],
    entry_points={
        'reviewboard.extensions':
        '%s = rbkarma.extension:RBKarmaExtension' % PACKAGE,
    },
    package_data={
        'rbkarma': [
            'htdocs/css/*.css',
            'htdocs/js/*.js',
            'templates/rbkarma/*.html',
            'templates/rbkarma/*.txt'
        ],
    },
    install_requires=['RB-Stats>=0.1']
)
