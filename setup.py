from setuptools import setup


setup(
    name='knocker',
    description='Port knocking client',
    version='0.1.0',
    entry_points={
        'console_scripts': ['knocker=knocker:main'],
    },
    author='Marco Rougeth',
    author_email='marco@rougeth.com',
    url='http://github.com/rougeh/knocker',
)
