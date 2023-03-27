from setuptools import setup

setup(
    name='hello_world',
    py_modules=['helloworld'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        hello=helloworld:hello
    ''',
)