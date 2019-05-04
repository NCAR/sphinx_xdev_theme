# -*- coding: utf-8 -*-
"""`sphinx_xdev_theme` lives on `Github`_.

.. _github: https://github.com/NCAR/sphinx_xdev_theme

"""

from setuptools import setup
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sphinx_xdev_theme',
    use_scm_version={'version_scheme': 'post-release', 'local_scheme': 'dirty-tag'},
    setup_requires=['setuptools_scm', 'setuptools>=30.3.0', 'setuptools_scm_git_archive'],
    url='https://github.com/NCAR/sphinx_xdev_theme/',
    python_requires='>=3.6',
    license='Apache License 2.0',
    maintainer='Anderson Banihirwe',
    maintainer_email='abanihi@ucar.edu',
    description='xdev theme for Sphinx',
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    packages=['sphinx_xdev_theme'],
    package_data={'sphinx_xdev_theme': [
        'theme.conf',
        '*.html',
        'static/*.css',
        'static/*.otf',
        'static/*.png'
    ]},
    include_package_data=True,
    # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
    entry_points = {
        'sphinx.html_themes': [
            'xdev = sphinx_xdev_theme',
        ]
    },
    install_requires=[
       'sphinx==1.8.4'
    ],
    classifiers=[
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)