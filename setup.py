from setuptools import setup

setup(name='xapitodict',
      version='0.2',
      packages=['xapitodict', 'xapitodict.cmd'],
      install_requires=["sexpdata", "xmltodict"],
      entry_points={
          'console_scripts': [
              'xapi-to-json = xapitodict.cmd.xapitojson:main'
          ]
      })
