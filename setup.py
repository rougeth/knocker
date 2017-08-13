from setuptools import find_packages, setup


setup(
    name='knocker',
    description='Port knocking client',
    version='0.1.2',
    py_modules=['knocker'],
    entry_points={
        'console_scripts': ['knocker=knocker:main'],
    },
    author='Marco Rougeth',
    author_email='marco@rougeth.com',
    url='http://github.com/rougeh/knocker',
)
