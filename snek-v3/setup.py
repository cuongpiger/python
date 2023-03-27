from setuptools import setup

setup(
    name='snek3',
    entry_points={
        'console_scripts': [
            'snek3 = snek:main',
        ],
    }
)
