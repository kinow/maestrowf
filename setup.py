from os import path
from maestrowf import __version__
from setuptools import setup, find_packages

setup(name='maestrowf',
      description='A tool and library for specifying and conducting general '
      'workflows.',
      version='1.1.4dev1.2',
      author='Francesco Di Natale',
      author_email='dinatale3@llnl.gov',
      url='https://github.com/llnl/maestrowf',
      license='MIT License',
      packages=find_packages(),
      entry_points={
        'console_scripts': [
                'maestro = maestrowf.maestro:main',
                'conductor = maestrowf.conductor:main',
        ]
    },
    install_requires=[
        'PyYAML>=4.2b1',
        'six',
        "filelock",
        "tabulate",
        "enum34 ; python_version<'3.4'",
        "dill",
        "jsonschema>=3.2.0",
        "coloredlogs",
        "chainmap ; python_version<'3'",
    ],
    extras_require={},
    long_description=load_readme(),
    long_description_content_type='text/markdown',
    download_url='https://pypi.org/project/maestrowf/',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'Topic :: System :: Distributed Computing',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    package_data={
        'maestrowf': [
            'maestrowf/specification/schemas/yamlspecification.json'
        ],
    },
    include_package_data=True,
)
