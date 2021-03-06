from setuptools import setup, find_packages
from pip.req import parse_requirements
from blockchain_certificates import __version__


install_reqs = parse_requirements('requirements.txt', session=False)
requirements = [str(ir.req) for ir in install_reqs]

setup(name='blockchain-certificates',
      version=__version__,
      description='Create pdf certificate files and issue on the blockchain!',
      author='Konstantinos Karasavvas',
      license='MIT',
      packages=['blockchain_certificates'],
      #packages=find_packages(),
      install_requires=requirements,
      package_data={
          'blockchain_certificates': ['java/itextpdf-5.5.10.jar',
                                      'java/ITEXTPDF-LICENSE.txt',
                                      'java/json-simple-1.1.1.jar',
                                      'java/JSON-SIMPLE-LICENSE.txt',
                                      'java/FillPdf.java',
                                      'java/FillPdf.class'],
      },
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'create-certificates = blockchain_certificates.create_certificates:main',
              'publish-hash = blockchain_certificates.publish_hash:main'
          ]
      }
     )

