from setuptools import setup, find_packages

setup(
    name='quart-oauth-client',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'quart',
        'blinker',
        # Add other dependencies here
    ],
)
