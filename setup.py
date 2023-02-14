import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='lrplots',
    version='0.7.0',
    author='Andy Hauser',
    author_email='Andreas.Hauser@LMU.de',
    license='LICENSE',
    description='Plot collection for Long Read Sequencing',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ahcm/longread_plots',
    packages=setuptools.find_packages(),
    scripts=['bin/lrplot'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'seaborn',
          'matplotlib!=3.6.1',
          'pandas'
    ],
)
