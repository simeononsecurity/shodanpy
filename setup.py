from setuptools import setup, find_packages

setup(
    name='shodanpy_simeononsecurity',
    version='0.0.2',
    author='SimeonOnSecurity',
    author_email='contact@simeononsecurity.ch',
    description='A Series of Python Modules for Interacting with the Shodan API',
    long_description='A Series of Python Modules for Interacting with the Shodan API',
    url='https://github.com/simeononsecurity/shodanpy',
    packages=find_packages(),
    install_requires=[
        'requests', 'dotenv'
    ],
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
