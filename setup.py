from setuptools import setup, find_packages

setup(
    name='jinja2_neverundefined',
    version='0.5.0',
    description='Jinja2 extension that never undefined',
    url='https://github.com/james4ever0/jinja_neverundefined',
    author='James Brown',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'Jinja2',
    ],
)