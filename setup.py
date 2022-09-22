from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cbpi4-dht22-temp-hum-sensor',
      version='0.0.1',
      description='CraftBeerPi4 Plugin for DHT22 / AM2302 temperature and CO2 sensor',
      author='Daniel van der Zee',
      author_email='daniel@ezee.org',
      url='https://github.com/DanZee/cbpi4-dht22-temp-hum-sensor.git',
      license='GPLv3',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-dht22-temp-hum-sensor': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-dht22-temp-hum-sensor'],
        install_requires=[
        'adafruit-circuitpython-dht'
  ],
  long_description=long_description,
  long_description_content_type='text/markdown'

     )
