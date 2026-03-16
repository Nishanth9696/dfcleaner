from setuptools import setup, find_packages

setup(
    name="dfcleaner",
    version="0.1.0",
    author="Nishanth K",
    description="Simple DataFrame cleaning toolkit",
    Long_description=open('README.md').read(),
    Long_description_content_type='text/markdown',
    packages=find_packages(),
    url='https://github.com/Nishanth9696/dfcleaner',
    classifiers=[
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
        ],
    install_requires=[
        "pandas"
    ],
    python_requires=">=3.8",
)