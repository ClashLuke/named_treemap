import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Lucas Nestler",
    author_email="github.namedtreemap@nestler.sh",
    name='namedtreemap',
    license='BSD',
    description='jax.tree_map, but for all datatypes and with input names',
    version='0.0.1',
    long_description=README,
    url='https://github.com/clashluke/namedtreemap',
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    long_description_content_type="text/markdown",
    install_requires=[],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)
