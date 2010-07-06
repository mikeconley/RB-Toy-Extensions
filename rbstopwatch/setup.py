from setuptools import setup

PACKAGE="RB-Stopwatch"
VERSION="0.1"

setup(
    name=PACKAGE,
    version=VERSION,
    description="""RB-Stopwatch extension for Review Board""",
    author="Mike Conley",
    packages=["rbstopwatch"],
    entry_points={
        'reviewboard.extensions':
        '%s = rbstopwatch.extension:RBStopwatchExtension' % PACKAGE,
    },
    package_data={
        'rbstopwatch': [
            'htdocs/css/*.css',
            'htdocs/js/*.js',
            'templates/rbstopwatch/*.html',
            'templates/rbstopwatch/*.txt'
        ],
    },
    install_requires=['RB-Stats>=0.1']
)
