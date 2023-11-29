from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
    
setup(
    name='NameVariablePrint',
    version='1.0.0.4',
    description='Print variable name and value when you debugging',
    long_description = long_description,
    long_description_content_type='text/markdown',
    author='Shawn_Park',
    author_email='psh990626@gmail.com',
    url='https://github.com/sanghyeon1/nvprint',
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=['pypi', 'NameVariablePrint', 'debugprint', 'print'],
    python_requires='>=3.6',
    package_data={},
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
