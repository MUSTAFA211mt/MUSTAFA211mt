from setuptools import setup, find_packages

setup(
    name='mt_amino_library',
    version='1.0.0',
    description='مكتبة mt_amino_library: مكتبة Python قوية لمعالجة البيانات',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='MUSTAFA',
    author_email='بريدك@example.com',
    url='https://github.com/username/mt_amino_library',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)