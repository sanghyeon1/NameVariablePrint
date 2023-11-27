from setuptools import setup, find_packages

setup(
    name='nvprint',
    version='1.0.0',
    description='debug print variable name and value when you debugging',
    author='Shawn_Park',
    author_email='psh990626@gmail.com',
    url='https://github.com/sanghyeon1/nvprint',
    install_requires=[],
    packages=find_packages(exclude=[]),
    keywords=['pypi', 'nvprint', 'debugprint', 'print'],
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
