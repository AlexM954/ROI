from setuptools import setup, find_packages

setup(
    name='roi',
    version='0.1',
    packages=find_packages(where='.'),
    install_requires=[
        'numpy',
    ],
    package_dir={'': '.'},
    description='Python implementatin of the ROI algorithm.',
    author='Alex M.',
    url='https://github.com/AlexM954/ROI.git',
    license='GPL-3.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
    ],
)
