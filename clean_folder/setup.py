from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1',
    description='this package sorts out files',
    url='https://github.com/VolodymyrTES',
    author='Volodymyr Kyryienko',
    author_email='v.kyryienko856790@gmail.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder = clean_folder.sort_out:sorting_files']}
)