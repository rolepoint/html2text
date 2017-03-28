# coding: utf-8
from setuptools import setup, Command, find_packages


class RunPyTests(Command):
    description = "run all tests for the package"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import pytest
        pytest.main()


setup(
    name="html2text",
    version=".".join(map(str, __import__('html2text').__version__)),
    description="Turn HTML into equivalent Markdown-structured text.",
    author="Aaron Swartz",
    author_email="me@aaronsw.com",
    maintainer='Alireza Savand',
    maintainer_email='alireza.savand@gmail.com',
    url='https://github.com/rolepoint/html2text/',
    cmdclass={'test': RunPyTests},
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points="""
        [console_scripts]
        html2text=html2text.cli:main
    """,
    license='GNU GPL 3',
    tests_require=['pytest'],
    packages=find_packages(exclude=['test']),
    include_package_data=True,
    zip_safe=False,
)
