from setuptools import setup
with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

setup(
   name='emm',
   version='1.0',
   description='Exceptional Model Mining implementation',
   author='MathynS',
   packages=['.'],
   install_requires=requirements
)
