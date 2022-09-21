from setuptools import find_packages, setup

setup(
    name='pyclone-vi_jw', # added "_jw"
    version='0.1.1',
    description='Fast method for inferring clonal population structure from SNV data.',
    author='Andrew Roth',
    author_email='andrewjlroth@gmail.com',
    url='https://github.com/jiw181/pyclone-vi_jw', # the original one is 'https://github.com/aroth85/pyclone-vi',
    packages=find_packages(),
    license='GPL v3',
    entry_points={
        'console_scripts': [
            'pyclone-vi= pyclone_vi.cli:main',
        ]
    }
)
