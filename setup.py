from distutils.core import setup

setup(name='mongoschema',
      packages=['mongoschema'],
      version='1.0.0',
      description='Python library for getting schema details of MongoDB collections',
      author='Nimesh Kiran, Utsav Tiwary',
      author_email='nimesh.aug11@gmail.com',
      url='https://github.com/nimeshkverma/mongo_schema',
      download_url='',
      py_modules=['mongoschema'],
      install_requires=['pymongo'],
      keywords=['mongo', 'schema'],
      classifiers=[],
      )
