from setuptools import setup, find_packages

setup(
    name='pbraw',
    version='0.1',
    description='A library to extract plaintexts from pastebins',
    url='https://github.com/Hummer12007/pbraw',
    author='Mykyta Holubakha',
    author_email='hilobakho@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['requests'],
    entry_points={
        'console_scripts':['pbraw = pbraw.main:main']
    }
)
