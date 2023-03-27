from setuptools import setup

setup(
    name='snek2',
    entry_points={
        'console_scripts': [
            'snek2 = snek:main',
        ],
    }
)
