from os.path import dirname, join
from setuptools import setup, find_packages

setup(
      name='IBP',
      version=1.0,
      url='https://github.com/wy49/663FinalProject-YZ',
      description='Infinite Latent Feature Models and the Indian Buffet Process',
      author='Wenwen Ye, Kuazhuo Zhang',
      license='BSD',
      packages=find_packages(exclude=('tests', 'tests.*')),
      include_package_data=True,
      zip_safe=False,
      entry_points={
      'console_scripts': ['scrapy = scrapy.cmdline:execute']
      },
      classifiers=[
                   'Framework :: IBP',
                   'Development Status :: 5 - Production/Stable',
                   'Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6',
                   'Topic :: Internet :: WWW/HTTP',
                   'Topic :: Software Development :: Libraries :: Application Frameworks',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   ],
      install_requires=[],
      )
