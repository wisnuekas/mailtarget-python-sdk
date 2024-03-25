# setup.py
from setuptools import setup, find_packages

setup(
    name='mailtarget_sdk',
    version='0.1.0',
    author='Wisnu Eka Saputra',
    author_email='wisnu.eka@mailtarget.co',
    description='SDK Python untuk Mailtarget API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='URL repository Anda',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Versi minimum Python yang didukung

)
