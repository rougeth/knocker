from setuptools import find_packages, setup


with open('README.md') as f:
    long_description = f.read()


setup(
    name='knocker',
    description='Port knocking client',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    version='0.1.4',
    py_modules=['knocker'],
    entry_points={
        'console_scripts': ['knocker=knocker:main'],
    },
    author='Marco Rougeth',
    author_email='marco@rougeth.com',
    url='http://github.com/rougeh/knocker',
)
