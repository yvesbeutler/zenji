from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Zenji',
    version='0.1.0',
    description='A solver for the riddles of the famous zenji video game',
    long_description=readme,
    author='Yves Beutler',
    author_email='yves.beutler@hotmail.com',
    url='https://github.com/yvesbeutler/zenji',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)