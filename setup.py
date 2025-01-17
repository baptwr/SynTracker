from setuptools import setup, find_packages

setup(
    name='syntracker',
    version='1.4.0',
    description='SynTracker is a pipeline, designated to determine the biological relatedness of conspecific strains (microbial strains of the same species) using genome synteny.',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'syntracker=syntracker:main',
            'syntracker_makeDB=syntracker_makeDB:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3',
)