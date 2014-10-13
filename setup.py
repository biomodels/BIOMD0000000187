from setuptools import setup, find_packages

setup(name='BIOMD0000000187',
      version=20140916,
      description='BIOMD0000000187 from BioModels',
      url='http://www.ebi.ac.uk/biomodels-main/BIOMD0000000187',
      maintainer='Stanley Gu',
      maintainer_url='stanleygu@gmail.com',
      packages=find_packages(),
      package_data={'': ['*.xml', 'README.md']},
    )